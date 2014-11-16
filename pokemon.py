#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import random, randrange
import moves
from moves import print_moves, move_choice
from pokedex import pokedex, pokemon_choice, poketype, poke_type_chart

class Pokemon(object):
    #Set the pokemon's name at the inicialization
    def __init__(self):
        sure = "No"
        while(sure == "No"):
            #Set your POKeMON's name and its respective types
            name = None
            types = None
            while name == None:
                print("\nPlease, enter with the desired POKeMON:\n")
                name = input()
                get_dictionary = pokemon_choice(name.title())
                if  get_dictionary == None:
                    name = None
                    print("\nInvalid name. Type a name of a pokemon from the first generation.\n")
                else:
                    for k, v in get_dictionary.items():
                        name = k
                        types = v
                        break
            split_string = types.split(' ')
            type1 = split_string[0]
            type2 = split_string[1]
            print("\nSo you have choosen a "+name+". Its types are "+type1+"/"+type2+". A nice choice!\n")
            #Set your POKeMON's level
            level = -1
            while level == -1:
                print("\nWhat is its level?\n")
                try:
                    level = int(input())
                    if level < 0 or level > 99:
                        level = -1
                        print("\nInvalid number. The level must be a number from 1 to 99. Let's retry this.\n")
                except ValueError:
                    print("\nNot a number. Let's retry this.\n")

            #Set your Pokemon moves
            i = 0
            print("\nLet's choose the skills for your pokemon. Here is a list of the skills you can choose:\n\n")
            print_moves()
            print("\nKeep in mind that your pokemon can only learn skills that are from his own type, unless the skill is of Normal type.\n")
            print("\nThis means that, for example, an Electric/Blank types pokemon can't learn a Fire type skill.\n")
            print("\nTo choose a skill, type its name using your keyboard. You will have to choose 4 skills for your pokemon.\n")
            while i < 5:
                if i == 0:
                    move0_name = 'Struggle'
                    move0_type = 'Normal'
                    move0_pp = 1
                    move0_power = 50
                    move0_accuracy = 100
                    i = i + 1
                    continue
                elif i == 1:
                    print("\nOk, now select your pokemons "+str(i)+"st skill.\n")
                    move1 = input()
                    get_dictionary = move_choice(move1.title())
                    if get_dictionary == None:
                        print("\nThere's no such skill. Let's retry this. Select your pokemons "+str(i)+"st skill.\n")
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
                            print("\nYou have selected the skill "+move1_name+". It is your pokemon's "+str(i)+"st skill. Very well!\n")
                            i = i + 1
                        else:
                            print("\nYour pokemon is of types "+type1+"/"+type2+" and can't learn the skill "+move1_name+" of type "+move1_type+".\n")
                elif i == 2:
                    print("\nNow select your pokemons "+str(i)+"nd skill.\n")
                    move2 = input()
                    get_dictionary = move_choice(move2.title())
                    if get_dictionary == None:
                        print("\nThere's no such skill. Let's retry this. Select your pokemons "+str(i)+"nd skill.\n")
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
                            print("\nYou already selected the skill "+move2_name+" previously and your pokemon already know it. Lets select another one.\n")
                        elif move2_type == "Normal" or move2_type == type1 or move2_type == type2:
                            print("\nYou have selected the skill "+move2_name+". It is your pokemon's "+str(i)+"nd skill. Splendid choice!\n")
                            i = i + 1
                        else:
                            print("\nYour pokemon is of types "+type1+"/"+type2+" and can't learn the skill "+move2_name+" of type "+move2_type+".\n")
                elif i == 3:
                    print("\nNow for your pokemons "+str(i)+"rd skill.\n")
                    move3 = input()
                    get_dictionary = move_choice(move3.title())
                    if get_dictionary == None:
                        print("\nThere's no such skill. Let's retry this. Select your pokemons "+str(i)+"rd skill.\n")
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
                            print("\nYou already selected the skill "+move3_name+" previously and your pokemon already know it. Lets select another one.\n")
                        elif move3_type == "Normal" or move3_type == type1 or move3_type == type2:
                            print("\nYou have selected the skill "+move3_name+". It is your pokemon's "+str(i)+"rd skill. Awesome!\n")
                            i = i + 1
                        else:
                            print("\nYour pokemon is of types "+type1+"/"+type2+" and can't learn the skill "+move3_name+" of type "+move3_type+".\n")
                else:
                    print("\nNow for your pokemons "+str(i)+"th and last skill.\n")
                    move4 = input()
                    get_dictionary = move_choice(move4.title())
                    if get_dictionary == None:
                        print("\nThere's no such skill. Let's retry this. Select your pokemons "+str(i)+"th skill.\n")
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
                            print("\nYou already selected the skill "+move4_name+" previously and your pokemon already know it. Lets select another one.\n")
                        elif move4_type == "Normal" or move4_type == type1 or move4_type == type2:
                            print("\nYou have selected the skill "+move4_name+". It is your pokemon's "+str(i)+"th and last skill. Well done!\n")
                            i = i + 1
                        else:
                            print("\nYour pokemon is of types "+type1+"/"+type2+" and can't learn the skill "+move4_name+" of type "+move4_type+".\n")
            #Set your POKeMON status, please use the official status
            print("\nNow let's set your POKeMON's status!\n")

            #Set HP
            print("\nHow much HP?\n")
            hp = int(input())
            #Set Attack
            print("\nHow much Attack?\n")
            attack = int(input())
            #Set Defense
            print("\nHow much Defense?\n")
            defense = int(input())
            #Set Special
            print("\nHow much Special?\n")
            special = int(input())
            #Set Speed
            print("\nHow much Speed?\n")
            speed = int(input())

            #Display the newborn POKeMON's info
            print("\nYour POKeMON status are:\n\n")
            print("\tName: "+name+" (Level %d)" %level)
            print()
            print("\tType1: "+type1+"\n\tType2: "+type2)
            print()
            print("\tHP: %d\n\tAttack: %d\n\tDefense: %d\n\tSpecial: %d\n\tSpeed: %d" %(hp, attack, defense, special, speed))
            print()
            print("\tMove 1: "+move1_name+": ("+move1_type+"/"+str(move1_pp)+"/"+str(move1_power)+"/"+str(move1_accuracy)+")\n")
            print("\tMove 2: "+move2_name+": ("+move2_type+"/"+str(move2_pp)+"/"+str(move2_power)+"/"+str(move2_accuracy)+")\n")
            print("\tMove 3: "+move3_name+": ("+move3_type+"/"+str(move3_pp)+"/"+str(move3_power)+"/"+str(move3_accuracy)+")\n")
            print("\tMove 4: "+move4_name+": ("+move4_type+"/"+str(move4_pp)+"/"+str(move4_power)+"/"+str(move4_accuracy)+")\n")
            print()
            print("Do you want to continue?\n(Yes or No)\n")
            #Check if user is sure about his options
            decision = "No"
            while decision.capitalize() == "No":
                decision = input()
                #User is not sure
                if(decision.capitalize() == "No"):
                    print("\nOk, let's do it again...\n\n")
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

                    #Set Moves
                    self.move0 = moves.Moves(move0_name, move0_type, move0_pp, move0_power, move0_accuracy, move0_pp) #Struggle
                    self.move1 = moves.Moves(move1_name, move1_type, move1_pp, move1_power, move1_accuracy, move1_pp)
                    self.move2 = moves.Moves(move2_name, move2_type, move2_pp, move2_power, move2_accuracy, move2_pp)
                    self.move3 = moves.Moves(move3_name, move3_type, move3_pp, move3_power, move3_accuracy, move3_pp)
                    self.move4 = moves.Moves(move4_name, move4_type, move4_pp, move4_power, move4_accuracy, move4_pp)
                    print("\nOk! Your POKeMON has been created! Let's continue!\n\n")
                    sure = "Yes"
                    decision = "Yes"
                #Troll user. You have to answer Yes or no!
                else:
                    print("\nWell... I was expecting for a Yes or a No, so please, don't make the things hard and answer my question, I don't have all day.\n")
                    decision = "No"


    def subtract_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0: self.hp = 0


    def is_defeated(self):
        if self.hp == 0:
            return True
        else:
            return False


    def perform_attack(self, opponent):
        #The user will choose his skill
        option = -1
        if self.move1.remaining_pp == 0 and self.move2.remaining_pp == 0 and self.move3.remaining_pp == 0 and self.move4.remaining_pp == 0:
            print("Your pokemon have no more PP left and will use Struggle!\n\n")
            option = 0

        while option == -1:
            self.print_attacks()
            print("Choose the attack:")
            try:
                option = int(input())
                if  option <= 0 or option >= 5:
                    option = -1
                    print("\nInvalid option! Type a number from 1 to 4.\n")
            except ValueError:
                print("\nInvalid option! Type a number from 1 to 4.\n")
        damage = self.calculate_and_subtract_damage(opponent, option)
        print(self.name + " inflicted " + str(damage) + " points of damage in " + opponent.name + "!")


    def calculate_and_subtract_damage(self, opponent, option):
        if option == 0:
            damage = self.calculate_damage(self.move0, opponent)
        elif option == 1:
            damage = self.calculate_damage(self.move1, opponent)
            self.move1.remaining_pp = self.move1.remaining_pp - 1
        elif option == 2:
            damage = self.calculate_damage(self.move2, opponent)
            self.move2.remaining_pp = self.move2.remaining_pp - 1
        elif option == 3:
            damage = self.calculate_damage(self.move3, opponent)
            self.move3.remaining_pp = self.move3.remaining_pp - 1
        elif option == 4:
            damage = self.calculate_damage(self.move4, opponent)
            self.move4.remaining_pp = self.move4.remaining_pp - 1
        opponent.subtract_damage(damage)
        return damage


    def print_attacks(self):
        print("It's " + self.name + "'s turn!")
        print("Attacks:")
        print("1. "+self.move1.move_name+" ("+str(self.move1.remaining_pp)+"/"+str(self.move1.move_pp)+")")
        print("2. "+self.move2.move_name+" ("+str(self.move2.remaining_pp)+"/"+str(self.move2.move_pp)+")")
        print("3. "+self.move3.move_name+" ("+str(self.move3.remaining_pp)+"/"+str(self.move3.move_pp)+")")
        print("4. "+self.move4.move_name+" ("+str(self.move4.remaining_pp)+"/"+str(self.move4.move_pp)+")")


    def calculate_damage(self, move, opponent):
        if self.type1 == move.move_type or self.type2 == move.move_type: stab = 1.5
        else: stab = 1.0

        #Verifies if the attack is critical
        crit = random()
        prob_crit = (self.speed/512)
        if(prob_crit <= crit): level = (2*self.level + 5)/(self.level+5) #TODO: Check if this is correct
        else: level = self.level

        #Find the modifier type
        m = move.move_type
        n = opponent.type1
        l = opponent.type2
        type_index = poketype()
        type_chart = poke_type_chart()
        for i in type_index:
            if i==m: index_attack = int(type_index[i])
            if i==n: index_defender1 = int(type_index[i])
            if l != 'Blank' and i==l: index_defender2 = type_index[i]

        type1_damage = type_chart[index_attack][index_defender1]
        if l != 'Blank': type2_damage = type_chart[index_attack][index_defender2]
        else: type2_damage = 0

        type_damage = type1_damage + type2_damage

        modifier = stab * type_damage * (randrange(85, 100, 1)/100)
        damage = int(((((2 * level) + 10) / 250) * (opponent.attack / opponent.defense) * move.move_power + 2) * modifier)

        return damage
