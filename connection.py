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

def local():
    global battle
    battle = Battle(local = True)


def client(server_address):
    global battle, pokemon_client, pokemon_server
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

        pokemon_client.print_attacks()
        while True:
            if pokemon_client.move1.remaining_pp == 0 and pokemon_client.move2.remaining_pp == 0 and pokemon_client.move3.remaining_pp == 0 and pokemon_client.move4.remaining_pp == 0:
                print("\nYour Pokemon have no more PP left to use his skills. Your Pokemon used Struggle.\n")
                option = 0
            else:
                print("Choose the attack: ")
                option = input()
                if option == '1' and pokemon_client.move1.remaining_pp > 0:
                    pokemon_client.move1.remaining_pp  -= 1
                    break
                elif option == '1' and pokemon_client.move1.remaining_pp <= 0:
                    print("You have no more available PP to use this skill!")
                elif option == '2' and pokemon_client.move2.remaining_pp > 0:
                    pokemon_client.move2.remaining_pp  -= 1
                    break
                elif option == '2' and pokemon_client.move1.remaining_pp <= 0:
                    print("You have no more available PP to use this skill!")
                elif option == '3' and pokemon_client.move3.remaining_pp > 0:
                    pokemon_client.move3.remaining_pp  -= 1
                    break
                elif option == '3' and pokemon_client.move1.remaining_pp <= 0:
                    print("You have no more available PP to use this skill!")
                elif option == '4' and pokemon_client.move4.remaining_pp > 0:
                    pokemon_client.move4.remaining_pp  -= 1
                    break
                elif option == '4' and pokemon_client.move1.remaining_pp <= 0:
                    print("You have no more available PP to use this skill!")
                else:
                    print("\nInvalid option. It needs to be a number from 1 to 4 with remaining PP.\n")
        xml = xml_pokemon.generate(pokemon_client, pokemon_server)
        response = requests.post('http://' + server_address + ':5000/battle/attack/' + option, data = xml, headers={'Content-Type': 'application/xml'})
        not_first_round = True


def server():
    print("Waiting for a client...")
    app.run()


@app.route("/battle", methods=['POST'])
def battle_start():
    global battle, pokemon_client, pokemon_server
    if battle == None: battle = Battle(server = True)
    else: abort(403)
    xml = request.data.decode('utf-8')
    pokemon_client, dummy = xml_pokemon.parse(xml)
    pokemon_server = Pokemon.create_pokemon()
    battle.print_battle_status(pokemon_client, pokemon_server)
    if pokemon_server.speed > pokemon_client.speed:
        option = pokemon_server.perform_attack_network(pokemon_client, -1)
        pokemon_server.announce_damage_network(pokemon_client, option)
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
        option = pokemon_server.perform_attack_network(pokemon_client, -1)
        pokemon_server.announce_damage_network(pokemon_client, option)
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
