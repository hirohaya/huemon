#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pokemon import Pokemon

class Battle(object):
    def __init__(self):
        pokemon1, pokemon2 = self.initialize_pokemons()
        self.begin_battle(pokemon1, pokemon2)


    def initialize_pokemons(self):
        print("Let's create the first POKeMON!")
        pokemon1 = Pokemon()
        print("Let's create the second POKeMON!")
        pokemon2 = Pokemon()
        return pokemon1, pokemon2


    def begin_battle(self, pokemon1, pokemon2):
        print("\n\n\nLet's begin the battle!")
        # pokemon1 should be the fastest
        if pokemon2.speed > pokemon1.speed:
            # swap
            pokemon_tmp = pokemon1
            pokemon1 = pokemon2
            pokemon2 = pokemon_tmp
        self.print_battle_status(pokemon1, pokemon2)
        while True:
           pokemon1.perform_attack(pokemon2)
           self.print_battle_status(pokemon1, pokemon2)
           if pokemon2.is_defeated:
               pass #end battle
           pokemon2.perform_attack(pokemon1)
           self.print_battle_status(pokemon1, pokemon2)
           if pokemon1.is_defeated:
               pass #end battle


    def print_battle_status(self, pokemon1, pokemon2):
        print("\nBattle status:")
        print(pokemon1.name + " has " + str(pokemon1.hp) + " HP.")
        print(pokemon2.name + " has " + str(pokemon2.hp) + " HP.\n")
