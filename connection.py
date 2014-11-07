#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from battle import Battle
from pokemon import Pokemon
import pokemons_xml
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
    pokemon = Pokemon()
    pkmn_xml = pokemons_xml.generate_pokemons_xml(pokemon)
    request = requests.post('http://' + server_address + ':5000/battle', data = pkmn_xml)
    while True:
        pkmn_xml = pokemons_xml.parse_pokemons_xml(request.content)
        # checa se batalha acabou
        # print battle status
        # print attacks
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
