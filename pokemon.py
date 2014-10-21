#!/usr/bin/env python
# -*- coding: utf-8 -*-

import moves
from myfunctions import print_char

class Pokemon(object):
	
	#Set the pokemon's name at the inicialization
	def __init__(self, name, level, type1, type2, hp, attack, defense, special, speed):
		self.name = name
		self.level = level
		self.type1 = type1
		self.type2 = type2
		
		#Set status on constructor
		self.hp = hp
		self.attack = attack
		self.defense = defense
		self.special = special
		self.speed = speed
		
#	#Set the pokemon's status
#	def status(self, hp, attack, defense, special, speed):
#		self.hp = hp
#		self.attack = attack
#		self.defense = defense
#		self.special = special
#		self.speed = speed
		
	#Set the pokemon's moves, moves are objects of Moves type for a better organization
	def moves(self, name1, name2, name3, name4):
		self.move1 = moves.Moves(name1)
		self.move2 = moves.Moves(name2)
		self.move3 = moves.Moves(name3)
		self.move4 = moves.Moves(name4)

#Method that guides the player to create a pokemon
#Please read and use the official rules		
def pokegen():

	print_char("Let's start by creating your POKeMON!\n")
	sure = "No"
	while(sure == "No"):
		#Set your POKeMON's name
		print_char("\nPlease, enter with the desired POKeMON:\n")
		name = str(raw_input())
		
		#Set your POKeMON's level
		print_char("\nWhat is its level?\n")
		level = int(raw_input())
		print ""
		#Set your POKeMON's type(s)
		print_char("\nWhat is its first type?\n")
		type1 = str(raw_input())
		print_char("\nIf it does have a second type, which one is it?"\
				   " If it has only one type, type 'Blank'.\n(Sorry for the pun)\n")
		type2 = str(raw_input())
		
		#Set your POKeMON status, please use the official status
		print_char("\nNow let's set your POKeMON's status!\n")
		
		#Set HP
		print_char("\nHow much HP?\n")
		hp = int(raw_input())
		#Set Attack
		print_char("\nHow much Attack?\n")
		attack = int(raw_input())
		#Set Defense
		print_char("\nHow much Defense?\n")
		defense = int(raw_input())
		#Set Special
		print_char("\nHow much Special?\n")
		special = int(raw_input())
		#Set Speed
		print_char("\nHow much Speed?\n")
		speed = int(raw_input())
		
		#Display the newborn POKeMON's info
		print_char("\nYour POKeMON status are:\n\n")
		print "\tName: "+name+" (Level %d)" %level
		print ""
		print "\tType1: "+type1+"\n\tType2: "+type2
		print ""
		print "\tHP: %d\n\tAttack: %d\n\tDefense: %d\n\tSpecial: %d\n\tSpeed: %d" %(hp, attack, defense, special, speed)
		print ""
		print_char("Do you want to continue?\n(Yes or No)\n")
		sure = raw_input()
		
		if(sure == "No"):
			print_char("\nOk, let's do it again...\n\n")
		
		#I'm assuming you are a good user and don't type anything else than Yes or No
		else:
			pokemon1 = Pokemon(name, level, type1, type2, hp, attack, defense, special, speed)
			print_char("\nOk! Your POKeMON has been created! Let's continue!\n\n")
			
	return pokemon1
