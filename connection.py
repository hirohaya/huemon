#!/usr/bin/env python
# -*- coding: utf-8 -*-

from battle import Battle
from pokemon import Pokemon
import xml_pokemon

import requests
from flask import Flask
app = Flask(__name__)

# disable flask server messages
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def local():
    Battle(local = True)


def client(server_address):
    battle = Battle()
    battle = Battle()
    pokemon = Pokemon()
    xml = xml_pokemon.generate(pokemon)
    response = requests.post('http://' + server_address + ':5000/battle', data = xml)
    while True:
        pokemon_client, pokemon_server = xml_pokemon.parse(response.content)
        if Battle.battle_ended(pokemon_client, pokemon_server): return
        Battle.print_battle_status(pokemon_client, pokemon_server)
        pokemon_client.print_attacks()
        option = input()
        response = requests.post('http://' + server_address + ':5000/battle/attack/' + option)


def server():
    #mudar pokemon constructor para apenas construir o objeto com parametros recebidos e criar metodo para o usuario inserir os dados para se criar um pokemon (e então chamar o constructor)
    #modificar battle para funcionar no modo server
    #implementar battle como singleton
    #implementar xml_pokemon
    #implementar server
    app.run()


@app.route("/battle", methods=['POST'])
def battle_start():
    pokemon_client = xml_pokemon.parse(xml)
    pokemon_server = Pokemon()
    if pokemon_server.speed > pokemon_client.speed:
        pokemon_server.perform_attack(pokemon_client)
    xml = xml_pokemon.generate(pokemon_client, pokemon_server)
    return xml


@app.route("/battle/attack/<int:attack_id>", methods=['POST'])
def battle_attack(attack_id):
    #depois while 1 recebe requisição de ataque:
    #    processa o ataque
    #    ataca
    #    devolve battle_state
    if attack_id == 0:
        return "attack 0"
    elif attack_id == 1: 
        return "attack 1"
    elif attack_id == 2: 
        return "attack 2"
    elif attack_id == 3: 
        return "attack 3"
    elif attack_id == 4: 
        return "attack 4"
        pass
