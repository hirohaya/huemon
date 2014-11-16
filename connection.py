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
    pokemon_client = Pokemon()
    xml = xml_pokemon.generate(pokemon_client)
    response = requests.post('http://' + server_address + ':5000/battle_state', data = xml, headers={'Content-Type': 'application/xml'})
    print("AQUI " + str(response.status_code))
    while response.status_code == 200:
        pokemon_client, pokemon_server = xml_pokemon.parse(response.content)
        if battle_ended(pokemon_client, pokemon_server): return
        battle.print_battle_status(pokemon_client, pokemon_server)
        pokemon_client.print_attacks()
        option = input()
        response = requests.post('http://' + server_address + ':5000/battle_state/attack/' + option)


def server():
    #mudar pokemon constructor para apenas construir o objeto com parametros recebidos
    #criar metodo para o usuario inserir os dados para se criar um pokemon (e então chamar o constructor)
    #implementar xml_pokemon
    app.run(debug=True)


@app.route("/battle_state", methods=['POST'])
def battle_start():
    global battle, pokemon_client, pokemon_server
    print(battle)
    if battle == None: battle = Battle(server = True)
    else: abort(403)
    xml = request.data.decode('utf-8')
    pokemon_client = xml_pokemon.parse(xml)
    pokemon_server = Pokemon()
    if pokemon_server.speed > pokemon_client.speed:
        pokemon_server.perform_attack(pokemon_client)
    xml = xml_pokemon.generate(pokemon_client, pokemon_server)
    return xml


@app.route("/battle_state/attack/<int:attack_id>", methods=['POST'])
def battle_attack(attack_id):
    pokemon_client.calculate_and_subtract_damage(pokemon_server, attack_id)
    pokemon_server.perform_attack(pokemon_client)
    xml = xml_pokemon.generate(pokemon_client, pokemon_server)
    return xml
