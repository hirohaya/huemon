#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from pokemon import *
from moves import *
from pokedex import *
from connection import *
from xml_pokemon import *

class TestPokemonTextGame(unittest.TestCase):
    def setUp(self):
        self.move0 = moves.create_move_dictionary(0, "Struggle", "Normal", 1, 50, 1.0, 1)
        self.move1 = moves.create_move_dictionary(1, "Psychic", "Psychic", 10, 90, 1.0, 10)
        self.move2 = moves.create_move_dictionary(2, "Psybeam", "Psychic", 20, 65, 1.0, 20)
        self.move3 = moves.create_move_dictionary(3, "Confusion", "Psychic", 25, 50, 1.0, 25)
        self.move4 = moves.create_move_dictionary(4, "Swift", "Normal", 20, 60, 1.0, 20)
        self.pokemon1 = Pokemon("Mew", "Psychic", "Blank", 100, 99, 20, 20, 20, 20, self.move0, self.move1, self.move2, self.move3, self.move4)
        self.pokemon2 = Pokemon("Mewtwo", "Psychic", "Blank", 200, 99, 25, 25, 25, 25, self.move0, self.move1, self.move2, self.move3, self.move4)
        self.damage = 40
        self.hp = self.pokemon1.hp

    def test_subtract_damage(self):
        expected_hp = self.pokemon1.hp - self.damage
        if expected_hp < 0:
            expected_hp = 0
        self.pokemon1.subtract_damage(self.damage)
        self.assertEqual(self.pokemon1.hp, expected_hp)


    def test_is_defeated(self):
        #Defeated
        self.pokemon1.hp = 0
        self.assertEqual(self.pokemon1.is_defeated(), True)
        #Not defeated
        self.pokemon1.hp = self.hp
        self.assertEqual(self.pokemon1.is_defeated(), False)


    def test_calculate_damage(self):
        expected_minimum_modifier = 0
        expected_maximum_modifier = 1.5 * 4 * 2 * 1

        expected_minimum_damage = int(((((2 * self.pokemon1.level) + 10) / 250) * (self.pokemon1.attack / self.pokemon2.defense) * self.pokemon1.move1.move_power + 2) * expected_minimum_modifier)
        expected_maximum_damage = int(((((2 * self.pokemon1.level) + 10) / 250) * (self.pokemon1.attack / self.pokemon2.defense) * self.pokemon1.move1.move_power + 2) * expected_maximum_modifier)
        #The damage must be inside a given interval, delimited by the maximum and minimum values of the modifier (as the rest of the formula is static to the respectives pokemons involved)
        self.assertGreaterEqual(self.pokemon1.calculate_damage(self.pokemon1.move1, self.pokemon2), expected_minimum_damage)
        self.assertLessEqual(self.pokemon1.calculate_damage(self.pokemon1.move1, self.pokemon2), expected_maximum_damage)
    
    #We know that move1 is Psychic and between pokemon1 and pokemon2, this is the strongest attack, 67.5 attack damage after modifiers applied
    #choose_attack_ai returns a move_id so we compare directely with move1.move_id
    def test_choose_attack_ai(self):
        self.assertEqual(self.pokemon1.choose_attack_ai(self.pokemon2), self.move1.move_id)
    
    #Once we know the type of both pokemons and their modifier, we can do a direct calculation of the damage
    #In this case, the selected attack is Psychic and it has an 90 atk base
    #Stab modifier = 1.5
    #Attack type modifier = .5
    #Total modifer = .75
    def test_calculate_damage_ai(self):
        expected_damage_ai = int(((((2 * self.pokemon1.level) + 10) / 250) * (self.pokemon1.attack / self.pokemon2.defense) * self.pokemon1.move1.move_power + 2) * .75)
        self.assertEqual(self.pokemon1.calculate_attack_ai(self.move1, self.pokemon2), expected_damage_ai)
        
if __name__ == '__main__':
    unittest.main()
