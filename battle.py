#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pokemon import Pokemon
from pprint import pprint

class Battle(object):
    def __init__(self):
        pokemon1, pokemon2 = self.initialize_pokemons()
        pprint(vars(pokemon1))
        self.begin_battle(pokemon1, pokemon2)
        pass

    def initialize_pokemons(self):
        pokemon1 = Pokemon()
        pokemon2 = Pokemon()
        return pokemon1, pokemon2
        pass

    def begin_battle(self, pokemon1, pokemon2):
        # pokemon1 should be the fastest
        if pokemon2.speed > pokemon1.speed:
            # swap
            pokemon_tmp = pokemon1
            pokemon1 = pokemon2
            pokemon2 = pokemon_tmp
        while True:
           pokemon1.perform_attack(pokemon1, pokemon2)
           if pokemon2.is_defeated:
               pass #end battle
           pokemon2.perform_attack(pokemon2, pokemon1)
           if pokemon1.is_defeated:
               pass #end battle
