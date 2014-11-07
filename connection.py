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
    Battle()


def client(server_address):
    battle = Battle()
    pokemon = Pokemon()
    xml = xml_pokemon.generate(pokemon)
    request = requests.post('http://' + server_address + ':5000/battle', data = xml)
    while True:
        pokemon_client, pokemon_server = xml_pokemon.parse(request.content)
        if Battle.battle_ended(pokemon_client, pokemon_server): return
        Battle.print_battle_status(pokemon_client, pokemon_server)
        pokemon_client.print_attacks()
        option = input()
        request = requests.post('http://' + server_address + ':5000/battle/attack/' + option)


def server():
    #inicia servidor e espera conexão
    #recebe conexão:
    #    recebe um battle_state com um pokemon
    #    constroi o outro pokemon
    #    monta o battle_state com 2 pokemons
    #    ve se começa atacando, ataca
    #    devolve battle_state
    #    depois while 1 recebe requisição de ataque:
    #        processa o ataque
    #        ataca
    #        devolve battle_state
    app.run()


@app.route("/battle", methods=['POST', 'GET'])
def battle_start():
    return "battle"
    pass


@app.route("/battle/attack/<int:attack_id>", methods=['POST', 'GET'])
def battle_attack(attack_id):
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
