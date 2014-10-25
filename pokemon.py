#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import moves
from pokedex import pokedex, pokemon_choice
from myfunctions import print_char

class Pokemon(object):
    #Set the pokemon's name at the inicialization
    def __init__(self):
        print_char("Let's start by creating your POKeMON!\n")
        sure = "No"
        while(sure == "No"):
            #Set your POKeMON's name and its respective types
            name = None
            types = None
            while name == None:
                print_char("\nPlease, enter with the desired POKeMON:\n")
                name = input()
                get_dictionary = pokemon_choice(name.capitalize())
                if  get_dictionary == None:
                    name = None
                    print_char("\nInvalid name. Type a name of a pokemon from the first generation.\n")
                else:
                    for k, v in get_dictionary.items():
                        name = k
                        types = v
                        break
            split_string = types.split(' ')
            type1 = split_string[0]
            type2 = split_string[1]
            print_char("\nSo you have choosen a "+name+". Its types are "+type1+"/"+type2+". A nice choice!\n")
            #Set your POKeMON's level
            level = -1
            while level == -1:
                print_char("\nWhat is its level?\n")
                try:
                    level = int(input())
                    if level < 0 or level > 99:
                        level = -1
                        print_char("\nInvalid number. The level must be a number from 1 to 99. Let's retry this.\n")
                except ValueError:
                    print_char("\nNot a number. Let's retry this.\n")

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
            #Check if user is sure about his options
            decision = "No"
            while decision.capitalize() == "No":
                decision = input() 
                #User is not sure
                if(decision.capitalize() == "No"):
                    print_char("\nOk, let's do it again...\n\n")
                    break
                #The user typed he is sure
                elif(decision.capitalize() == "Yes"):
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
                    sure = "Yes"
                    decision = "Yes"
                #Troll user. You have to answer Yes or no!
                else:
                    print_char("\nWell... I was expecting for a Yes or a No, so please, don't make the things hard and answer my question, I don't have all day.\n")
                    decision = "No"

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
