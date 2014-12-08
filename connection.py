#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from battle import Battle
from pokemon import Pokemon
import xml_pokemon

import requests
from flask import Flask, abort, request
app = Flask(__name__)

# disable flask server messages
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

battle = None
pokemon_client = None
pokemon_server = None
player = None

def local():
    global battle
    battle = Battle(local = True)


def client(server_address, local_player):
    global battle, pokemon_client, pokemon_server, player
    player = local_player
    battle = Battle(client = True)
    pokemon_client = Pokemon.create_pokemon()
    xml = xml_pokemon.generate(pokemon_client, pokemon_server)
    response = requests.post('http://' + server_address + ':5000/battle', data = xml, headers={'Content-Type': 'application/xml'})
    not_first_round = False
    while response.status_code == 200:
        if not_first_round:
            server_hp = pokemon_server.hp
            dummy, pokemon_server = xml_pokemon.parse(response.content.decode('utf-8'))
            print (pokemon_client.name + " inflicted " + str(server_hp - pokemon_server.hp) + " points of damage in " + pokemon_server.name + "!")
            battle.print_battle_status(pokemon_client, pokemon_server)
            if battle.battle_ended(pokemon_client, pokemon_server):
                return

            client_hp = pokemon_client.hp
            pokemon_client, dummy = xml_pokemon.parse(response.content.decode('utf-8'))
            print (pokemon_server.name + " inflicted " + str(client_hp - pokemon_client.hp) + " points of damage in " + pokemon_client.name + "!")
            battle.print_battle_status(pokemon_client, pokemon_server)
            if battle.battle_ended(pokemon_client, pokemon_server):
                return
        else:
            pokemon_client, pokemon_server = xml_pokemon.parse(response.content.decode('utf-8'))
            battle.print_battle_status(pokemon_client, pokemon_server)

        if player == "user":
            option = pokemon_client.perform_attack_client()
        elif player == "ai":
            option = pokemon_client.perform_attack_client_ai(pokemon_server)
        xml = xml_pokemon.generate(pokemon_client, pokemon_server)
        response = requests.post('http://' + server_address + ':5000/battle/attack/' + option, data = xml, headers={'Content-Type': 'application/xml'})
        not_first_round = True


def server(local_player):
    global player
    player = local_player
    print("Waiting for a client...")
    app.run()


@app.route("/battle", methods=['POST'])
def battle_start():
    global battle, pokemon_client, pokemon_server, player
    if battle == None: battle = Battle(server = True)
    else: abort(403)
    xml = request.data.decode('utf-8')
    pokemon_client, dummy = xml_pokemon.parse(xml)
    pokemon_server = Pokemon.create_pokemon()
    battle.print_battle_status(pokemon_client, pokemon_server)
    if pokemon_server.speed > pokemon_client.speed:
        if player == "user":
            option = pokemon_server.perform_attack_server()
        elif player == "ai":
            option = pokemon_server.perform_attack_server_ai(pokemon_client)
        pokemon_server.inflict_and_announce_damage_server(pokemon_client, option)
        battle.print_battle_status(pokemon_client, pokemon_server)
        if battle.battle_ended(pokemon_client, pokemon_server):
            server_shutdown()
    xml = xml_pokemon.generate(pokemon_client, pokemon_server)
    return xml


@app.route("/battle/attack/<int:attack_id>", methods=['POST'])
def battle_attack(attack_id):
    server_hp = pokemon_server.hp
    pokemon_client.calculate_and_subtract_damage(pokemon_server, attack_id)
    print (pokemon_client.name + " inflicted " + str(server_hp - pokemon_server.hp) + " points of damage in " + pokemon_server.name + "!")
    battle.print_battle_status(pokemon_client, pokemon_server)
    if battle.battle_ended(pokemon_client, pokemon_server):
        server_shutdown()
    else:
        if player == "user":
            option = pokemon_server.perform_attack_server()
        elif player == "ai":
            option = pokemon_server.perform_attack_server_ai(pokemon_client)
        pokemon_server.inflict_and_announce_damage_server(pokemon_client, option)
        battle.print_battle_status(pokemon_client, pokemon_server)
        if battle.battle_ended(pokemon_client, pokemon_server):
            server_shutdown()
    xml = xml_pokemon.generate(pokemon_client, pokemon_server)
    return xml

def server_shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
