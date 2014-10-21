#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pokemon
import interface

#This is a test

interface.oak_intro()
pokemon1 = pokemon.pokegen()








#Pikachu I choose you!!!
#pikachu = pokemon.Pokemon("Pikachu", 100, "Electric", "Blank", 35, 55, 30, 50, 90)

#Status 
#	HP: 35
#	Attack: 55
#	Defense: 30
#	Special: 50
#	Speed: 90
#pikachu.status(35, 55, 30, 50, 90)

#Moves (Name: Type Attack Accuracy PP)
#	Thundershock: Electric 40 100 30
#	Slam: Normal 80 75 20
#	No move
#	Quick Attack: Normal 40 100 30
#pikachu.moves("Thundershock", "Slam", "No move", "Quick Attack")

#Thundershock
#pikachu.move1.type("Electric")
#pikachu.move1.status(40, 100, 30)

#Slam
#pikachu.move2.type("Normal")
#pikachu.move2.status(80, 75, 20)

#No move
#pikachu.move3.type(1)
#pikachu.move3.status(1, 1, 1)

#Quick Attack
#pikachu.move4.type("Normal")
#pikachu.move4.status(40, 100, 30)

#Display Pikachu's info
#print "\nPikachu's Info:"
#print "\tName: "+pikachu.name+" (Level %d)" %pikachu.level
#print ""
#print "\tType1: "+pikachu.type1+"\n\tType2: "+pikachu.type2
#print ""
#print "\tHP: %d\n\tAttack: %d\n\tDefense: %d\n\tSpecial: %d\n\tSpeed: %d" %(pikachu.hp, pikachu.attack, pikachu.defense, pikachu.special, pikachu.speed)
#print ""
#print "\tMove1: "+pikachu.move1.name+" (%d/%d)"%(pikachu.move1.pp, pikachu.move1.pp), "- "+pikachu.move1.type
#print "\tMove2: "+pikachu.move2.name+" (%d/%d)"%(pikachu.move2.pp, pikachu.move2.pp), "- "+pikachu.move2.type
#print "\tMove3: "+pikachu.move3.name+" (%d/%d)"%(pikachu.move3.pp, pikachu.move3.pp), "- "+pikachu.move3.type
#print "\tMove4: "+pikachu.move4.name+" (%d/%d)"%(pikachu.move4.pp, pikachu.move4.pp), "- "+pikachu.move4.type
#print ""