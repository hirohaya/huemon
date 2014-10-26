#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from pokemon import *
from moves import *
from pokedex import *
from pprint import pprint

class TestPokemonTextGame(unittest.TestCase):
	
	def setUp(self):
		self.pokemon1 = Pokemon()
		self.pokemon2 = Pokemon()
		self.damage = 40
		self.hp = self.pokemon1.hp

	#def test_subtract_damage(self):
	#	expected_hp = self.pokemon1.hp - self.damage
	#	if expected_hp < 0:
	#		expected_hp = 0
	#	self.pokemon1.subtract_damage(self.damage)
	#	self.assertEqual(self.pokemon1.hp, expected_hp)

	#def test_is_defeated(self):
	#	#Derrotado
	#	self.pokemon1.hp = 0
	#	self.assertEqual(self.pokemon1.is_defeated(), True)
	#	#Nao Derrotado
	#	self.pokemon1.hp = self.hp
	#	self.assertEqual(self.pokemon1.is_defeated(), False)

	#def test_calculate_damage(self):
	#	expected_minimum_modifier = 0
	#	expected_maximum_modifier = 1.5 * 4 * 2 * 1 
	#
	#	expected_minimum_damage = int(((((2 * self.pokemon1.level) + 10) / 250) * (self.pokemon1.attack / self.pokemon2.defense) * self.pokemon1.move1.move_power + 2) * expected_minimum_modifier)
	#	expected_maximum_damage = int(((((2 * self.pokemon1.level) + 10) / 250) * (self.pokemon1.attack / self.pokemon2.defense) * self.pokemon1.move1.move_power + 2) * expected_maximum_modifier)
	#	#The damage must be inside a given interval, delimited by the maximum and minimum values of the modifier (as the rest of the formula is static to the respectives pokemons involved)
	#	self.assertGreaterEqual(self.pokemon1.calculate_damage(self.pokemon1.move1, self.pokemon2), expected_minimum_damage)
	#	self.assertLessEqual(self.pokemon1.calculate_damage(self.pokemon1.move1, self.pokemon2), expected_maximum_damage)


if __name__ == '__main__':
    unittest.main()