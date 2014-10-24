#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import system
from myfunctions import print_char
from time import sleep

#OAK's introduction from POKeMON Red/Blue/Green
def oak_intro():
    system('clear')
    intro_text1 = "OAK: Welcome to the world of POKeMON!\n\n"
    intro_text2 = "     My name is OAK!\n"\
                  "     People call me the POKeMON PROF!\n\n"
    intro_text3 = "     This world is inhabited by creatures called POKeMON!\n"\
                  "     For some people POKeMON are pets.\n"\
                  "     Others use them for fights.\n\n"
    intro_text4 = "     Myself...\n"\
                  "     I study POKeMON as a profession.\n\n"
    intro_text5 = "     First, what is your name?\n\n     "

    intro_text = (intro_text1, intro_text2, intro_text3, intro_text4)

    for text in intro_text:
        print_char(text)

    print_char(intro_text5)

    player_name = str(raw_input())

    print_char("\n     Right! So your name is "+player_name+"!\n\n")
    print_char("     "+player_name+"!\n     Your very own POKeMON legend is about to unfold!\n"\
               "     A world of dreams and adventures with POKeMON awaits! Let's go!\n\n")
            
    sleep(3)
    system('clear')
