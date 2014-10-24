#!/usr/bin/env python
# -*- coding: utf-8 -*-

import moves
from myfunctions import print_char

class Pokemon(object):
    #Set the pokemon's name at the inicialization
    def __init__(self):
        print_char("Let's start by creating your POKeMON!\n")
        sure = "No"
        while(sure == "No"):
            #Set your POKeMON's name
            print_char("\nPlease, enter with the desired POKeMON:\n")
            name = str(input())
            
            #Set your POKeMON's level
            print_char("\nWhat is its level?\n")
            level = int(input())
            print()
            #Set your POKeMON's type(s)
            print_char("\nWhat is its first type?\n")
            type1 = str(input())
            print_char("\nIf it does have a second type, which one is it?"\
                       " If it has only one type, type 'Blank'.\n(Sorry for the pun)\n")
            type2 = str(input())
            
            #Set your POKeMON status, please use the official status
            print_char("\nNow let's set your POKeMON's status!\n")
            
            #Set HP
            print_char("\nHow much HP?\n")
            hp = int(input())
            #Set Attack
            print_char("\nHow much Attack?\n")
            attack = int(input())
            #Set Defense
            print_char("\nHow much Defense?\n")
            defense = int(input())
            #Set Special
            print_char("\nHow much Special?\n")
            special = int(input())
            #Set Speed
            print_char("\nHow much Speed?\n")
            speed = int(input())
            
            #Display the newborn POKeMON's info
            print_char("\nYour POKeMON status are:\n\n")
            print("\tName: "+name+" (Level %d)" %level)
            print()
            print("\tType1: "+type1+"\n\tType2: "+type2)
            print()
            print("\tHP: %d\n\tAttack: %d\n\tDefense: %d\n\tSpecial: %d\n\tSpeed: %d" %(hp, attack, defense, special, speed))
            print()
            print_char("Do you want to continue?\n(Yes or No)\n")
            sure = input()
            
            if(sure == "No"):
                print_char("\nOk, let's do it again...\n\n")
            #I'm assuming you are a good user and don't type anything else than Yes or No
            else:
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
                print_char("\nOk! Your POKeMON has been created! Let's continue!\n\n")
        
    ##Set the pokemon's status
    #def status(self, hp, attack, defense, special, speed):
    #    self.hp = hp
    #    self.attack = attack
    #    self.defense = defense
    #    self.special = special
    #    self.speed = speed
        
    #Set the pokemon's moves, moves are objects of Moves type for a better organization
    def moves(self, name1, name2, name3, name4):
        self.move1 = moves.Moves(name1)
        self.move2 = moves.Moves(name2)
        self.move3 = moves.Moves(name3)
        self.move4 = moves.Moves(name4)

    def subtract_damage(self, damage):
        self.hp -= damage

    def is_defeated(self):
        if self.hp <= 0:
            return True
        else:
            return False

    def attack(self, opponent):
        # this is just an incomplete draft
        print("Choose the attack:")
        self.calculate_damage(attack)
        opponent.subtract_damage(damage)
        pass

    def calculate_damage(self):
        # here goes the formula
        pass
