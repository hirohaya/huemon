#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import moves
from moves import print_moves, move_choice
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

            #Set your Pokemon moves
            i = 0
            print_char("\nLet's choose the skills for your pokemon. Here is a list of the skills you can choose:\n\n")
            print_moves()
            print_char("\nKeep in mind that your pokemon can only learn skills that are from his own type, unless the skill is of Normal type.\n")
            print_char("\nThis means that, for example, an Electric/Blank types pokemon can't learn a Fire type skill.\n")
            print_char("\nTo choose a skill, type its name using your keyboard. You will have to choose 4 skills for your pokemon.\n")
            while i < 5:
                if i == 0:
                    move0 = 'Struggle'
                    type_move0 = 'Normal'
                    pp_move0 = 1
                    power_move0 = 50
                    accuracy_move0 = 100
                    i = i + 1
                    continue
                elif i == 1:
                    print_char("\nOk, now select your pokemons "+str(i)+"st skill.\n")
                    move1 = input()
                    get_dictionary = move_choice(move1)
                    if get_dictionary == None:
                        print_char("\nThere's no such skill. Let's retry this. Select your pokemons "+str(i)+"st skill.\n")
                    else:
                        for k, v in get_dictionary.items():
                            move1_name = k
                            move1_status = v
                            break
                        split_string = move1_status.split('/')
                        move1_type = split_string[0]
                        move1_pp = int(split_string[1])
                        move1_power = int(split_string[2])
                        move1_accuracy = float(split_string[3]) / 100.0
                        if move1_type == "Normal" or move1_type == type1 or move1_type == type2:
                            print_char("\nYou have selected the skill "+move1_name+". It is your pokemon's "+str(i)+"st skill. Very well!\n")
                            i = i + 1
                        else:
                            print_char("\nYour pokemon is of types "+type1+"/"+type2+" and can't learn the skill "+move1_name+" of type "+move1_type+".\n")
                elif i == 2:
                    print_char("\nNow select your pokemons "+str(i)+"nd skill.\n")
                    move2 = input()
                    get_dictionary = move_choice(move2)
                    if get_dictionary == None:
                        print_char("\nThere's no such skill. Let's retry this. Select your pokemons "+str(i)+"nd skill.\n")
                    else:
                        for k, v in get_dictionary.items():
                            move2_name = k
                            move2_status = v
                            break
                        split_string = move2_status.split('/')
                        move2_type = split_string[0]
                        move2_pp = int(split_string[1])
                        move2_power = int(split_string[2])
                        move2_accuracy = float(split_string[3]) / 100.0
                        if move2_name == move1_name:
                            print_char("\nYou already selected the skill "+move2_name+" previously and your pokemon already know it. Lets select another one.\n")
                        elif move2_type == "Normal" or move2_type == type1 or move2_type == type2:
                            print_char("\nYou have selected the skill "+move2_name+". It is your pokemon's "+str(i)+"nd skill. Splendid choice!\n")
                            i = i + 1
                        else:
                            print_char("\nYour pokemon is of types "+type1+"/"+type2+" and can't learn the skill "+move2_name+" of type "+move2_type+".\n")
                elif i == 3:
                    print_char("\nNow for your pokemons "+str(i)+"rd skill.\n")
                    move3 = input()
                    get_dictionary = move_choice(move3)
                    if get_dictionary == None:
                        print_char("\nThere's no such skill. Let's retry this. Select your pokemons "+str(i)+"rd skill.\n")
                    else:
                        for k, v in get_dictionary.items():
                            move3_name = k
                            move3_status = v
                            break
                        split_string = move3_status.split('/')
                        move3_type = split_string[0]
                        move3_pp = int(split_string[1])
                        move3_power = int(split_string[2])
                        move3_accuracy = float(split_string[3]) / 100.0
                        if move3_name == move2_name or move3_name == move1_name:
                            print_char("\nYou already selected the skill "+move3_name+" previously and your pokemon already know it. Lets select another one.\n")
                        elif move3_type == "Normal" or move3_type == type1 or move3_type == type2:
                            print_char("\nYou have selected the skill "+move3_name+". It is your pokemon's "+str(i)+"rd skill. Awesome!\n")
                            i = i + 1
                        else:
                            print_char("\nYour pokemon is of types "+type1+"/"+type2+" and can't learn the skill "+move3_name+" of type "+move3_type+".\n")
                else:
                    print_char("\nNow for your pokemons "+str(i)+"th and last skill.\n")
                    move4 = input()
                    get_dictionary = move_choice(move4)
                    if get_dictionary == None:
                        print_char("\nThere's no such skill. Let's retry this. Select your pokemons "+str(i)+"th skill.\n")
                    else:
                        for k, v in get_dictionary.items():
                            move4_name = k
                            move4_status = v
                            break
                        split_string = move4_status.split('/')
                        move4_type = split_string[0]
                        move4_pp = int(split_string[1])
                        move4_power = int(split_string[2])
                        move4_accuracy = float(split_string[3]) / 100.0
                        if move4_name == move3_name or move4_name == move2_name or move4_name == move1_name:
                            print_char("\nYou already selected the skill "+move4_name+" previously and your pokemon already know it. Lets select another one.\n")
                        elif move4_type == "Normal" or move4_type == type1 or move4_type == type2:
                            print_char("\nYou have selected the skill "+move4_name+". It is your pokemon's "+str(i)+"th and last skill. Well done!\n")
                            i = i + 1
                        else:
                            print_char("\nYour pokemon is of types "+type1+"/"+type2+" and can't learn the skill "+move4_name+" of type "+move4_type+".\n")
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
            print("Move 1: "+move1_name+": ("+move1_type+"/"+str(move1_pp)+"/"+str(move1_power)+"/"+str(move1_accuracy)+")\n")
            print("Move 2: "+move2_name+": ("+move2_type+"/"+str(move2_pp)+"/"+str(move2_power)+"/"+str(move2_accuracy)+")\n")
            print("Move 3: "+move3_name+": ("+move3_type+"/"+str(move3_pp)+"/"+str(move3_power)+"/"+str(move3_accuracy)+")\n")
            print("Move 4: "+move4_name+": ("+move4_type+"/"+str(move4_pp)+"/"+str(move4_power)+"/"+str(move4_accuracy)+")\n")
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
        
    #Set the pokemon's moves, moves are objects of Moves type for a better organization
    #def moves(self, name1, name2, name3, name4):
    #    self.move1 = moves.Moves(name1)
    #    self.move2 = moves.Moves(name2)
    #    self.move3 = moves.Moves(name3)
    #    self.move4 = moves.Moves(name4)

    def subtract_damage(self, damage):
        self.hp -= damage

    def is_defeated(self):
        if self.hp <= 0:
            return True
        else:
            return False

    def perform_attack(self, attacker, opponent):
        # this is just an incomplete draft
        print("Choose the attack:")
        # here goes the moves

        # here we finally calculate the attack action damage
        self.calculate_damage(attacker.level, attacker.attack, opponent.defense)
        opponent.subtract_damage(damage)
        pass

    def calculate_damage(self, attacker_level, attacker_attack, defender_defense):
        # here goes the formula
        base = 10 #will be deleted. Base is supposed to be "the base damage of the attack"
        modifier = 2 #same
        (((2 * level) + 10) / 250) * (attacker_attack / attacker.defense) * base + 2
        pass
