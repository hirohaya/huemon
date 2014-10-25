#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Defines pokemon's moves	
class Moves(object):
    #Set move name by inicialization
    def __init__(self, name):
        self.name = name
            
    #Set move type, in the future this will determine if the move will be super effective or not
    def type(self, type):
        if self.name == "No move":
            self.type = "Blank"
        else:
            self.type = type
                    
    #Moved pp to status
    def status(self, attack, accuracy, pp):
        if self.name == "No move":
            self.attack = 0
            self.accuracy = 0
            self.pp = 0
                
        else:
            self.attack = attack
            self.accuracy = accuracy
            self.pp = pp
