#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from battle import Battle

from flask import Flask
app = Flask(__name__)
# disable flask server messages
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def local():
    Battle()


def client(server_address):
    pass


def server():
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
