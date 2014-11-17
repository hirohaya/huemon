#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Defines pokemon's moves	
class Moves(object):
    #Set move name by inicialization
    def __init__(self, move_id, move_name, move_type, move_pp, move_power, move_acc, remaining_pp):
        self.move_id      = move_id
        self.move_name    = move_name
        self.move_type    = move_type
        self.move_pp      = move_pp
        self.move_power   = move_power
        self.move_acc     = move_acc 
        self.remaining_pp = remaining_pp


def pokemon_moves_list():
    #Ability Name/Ability Type/PP/Power/Accuracy. Source: http://www.psypokes.com/rby/attacks.php
    #Abilities with 'N/A' field are not being implemented, just the ones that inflicts damage (with no special effect)
    moves_list = {'Absorb': 'Grass/20/20/100',
                'Acid': 'Poison/30/40/100',
                'Aurora Beam': 'Ice/20/65/100',
                'Bind': 'Normal/20/15/75',
                'Bite': 'Normal/25/60/100',
                'Blizzard': 'Ice/5/120/90',
                'Body Slam': 'Normal/15/85/100',
                'Bone Club': 'Ground/20/65/85',
                'Bonemerang': 'Ground/10/50/90',
                'Bubble': 'Water/30/20/100',
                'Bubblebeam': 'Water/20/65/100',
                'Clamp': 'Water/10/35/75',
                'Confusion': 'Psychic/25/50/100',
                'Constrict': 'Normal/35/10/100',
                'Crabhammer': 'Water/10/90/85',
                'Cut': 'Normal/30/50/55',
                'Dig': 'Ground/10/100/100',
                'Dizzy Punch': 'Normal/10/70/100',
                'Double Kick': 'Fighting/30/30/100',
                'Double-Edge': 'Normal/15/100/100',
                'Doubleslap': 'Normal/10/15/85',
                'Dragon Rage': 'Dragon/10/60/100', #modified
                'Drill Peck': 'Flying/20/80/100',
                'Earthquake': 'Ground/10/100/100',
                'Egg Bomb': 'Normal/10/100/75',
                'Ember': 'Fire/25/40/100',
                'Fire Blast': 'Fire/20/120/85',
                'Fire Punch': 'Fire/15/75/100',
                'Flamethrower': 'Fire/15/95/100',
                'Fly': 'Flying/15/70/95',
                'Gust': 'Normal/35/40/100',
                'Headbutt': 'Normal/15/70/100',
                'Hi Jump Kick': 'Fighting/20/85/95',
                'Horn Attack': 'Normal/25/65/100',
                'Hydro Pump': 'Water/5/120/80',
                'Hyper Beam': 'Normal/5/150/90',
                'Hyper Fang': 'Normal/15/80/90',
                'Ice Beam': 'Ice/10/95/100',
                'Ice Punch': 'Ice/15/75/100',
                'Jump Kick': 'Fighting/20/70/95',
                'Karate Chop': 'Normal/25/55/100',
                'Lick': 'Ghost/30/20/100',
                'Low Kick': 'Fighting/20/50/90',
                'Mega Drain': 'Grass/10/40/100',
                'Mega Kick': 'Normal/5/120/75',
                'Mega Punch': 'Normal/20/80/85',
                'Pay Day': 'Normal/20/40/100',
                'Peck': 'Flying/35/35/100',
                'Petal Dance': 'Grass/20/70/100',
                'Pin Missile': 'Bug/20/70/85', #modified
                'Poison Sting': 'Poison/35/15/100',
                'Pound': 'Normal/35/40/100',
                'Psybeam': 'Psychic/20/65/100',
                'Psychic': 'Psychic/10/90/100',
                'Quick Attack': 'Normal/30/40/100',
                'Rage': 'Normal/20/20/100',
                'Razor Leaf': 'Grass/25/55/95',
                'Razor Wind': 'Normal/10/80/75',
                'Rock Slide': 'Rock/10/75/90',
                'Rock Throw': 'Rock/15/50/90',
                'Rolling Kick': 'Fighting/15/60/85',
                'Scratch': 'Normal/35/40/100',
                'Skull Bash': 'Normal/15/100/100',
                'Sky Attack': 'Flying/15/140/90',
                'Slam': 'Normal/20/80/75',
                'Slash': 'Normal/20/70/100',
                'Sludge': 'Poison/20/65/100',
                'Smog': 'Poison/20/20/100',
                'Solarbeam': 'Grass/10/120/100',
                'Stomp': 'Normal/20/65/100',
                'Strength': 'Normal/15/80/100',
                'Submission': 'Normal/20/80/80',
                'Surf': 'Water/15/95/100',
                'Swift': 'Normal/20/60/100',
                'Tackle': 'Normal/35/35/95',
                'Take Down': 'Normal/20/90/85',
                'Thrash': 'Normal/20/90/100',
                'Thunder': 'Electric/10/120/70',
                'Thunderbolt': 'Electric/15/95/100',
                'Thunderpunch': 'Electric/15/75/100',
                'Thundershock': 'Electric/15/40/100',
                'Tri Attack': 'Normal/10/80/100',
                'Twineedle': 'Bug/20/25/100',
                'Vicegrip': 'Normal/30/55/100',
                'Vine Whip': 'Grass/10/35/100',
                'Water Gun': 'Water/25/40/100',
                'Waterfall': 'Water/15/80/100',
                'Wing Attack': 'Flying/35/35/100'}
    return moves_list


def print_moves():
    print("Skill Name: Type/PP/Power/Accuracy")
    moves_list = pokemon_moves_list()
    for i in moves_list:
        print(i + ": "+ moves_list[i])


def move_choice(choosen_move):
    moves_list = pokemon_moves_list()
    i = 0
    for i in moves_list:
        if i == choosen_move:
            return {i: moves_list[i]}
    return None 


def move_type(move):
    moves_list = pokemon_moves_list()

    for i in moves_list:
        if i == move:
            attributes = moves_list[i]
            split_string = attribute.split('/')
            type = split_string[0]
            return type
    return None
