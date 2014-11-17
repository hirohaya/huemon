#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.etree import ElementTree
from pokemon import Pokemon
import moves
from moves import create_move_dictionary

def generate(pokemon1, pokemon2 = None):
    tree = ElementTree.parse('structure.xml')
    root = tree.getroot()
    xml_file = open('pokemon.xml', 'w')
    i = 0
    j = 0
    k = 0
    for child in root.iter():
        #client pokemon
        if k == 0:
            if child.tag == "battle_state":
                xml_file.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n")
                xml_file.write("<battle_state>\n")
                continue
            if child.tag == "pokemon":
                xml_file.write("  <pokemon>\n")
                continue
            if child.tag == "name" and i == 0:
                xml_file.write("    <name>"+pokemon1.name+"</name>\n")
                i = i + 1
                continue
            if child.tag == "level":
                xml_file.write("    <level>"+str(pokemon1.level)+"</level>\n")
                continue
            if child.tag == "health":
                xml_file.write("    <attributes>\n")
                xml_file.write("      <health>"+str(pokemon1.hp)+"</health>\n")
                continue
            if child.tag == "attack":
                xml_file.write("      <attack>"+str(pokemon1.attack)+"</attack>\n")
                continue
            if child.tag == "defense":
                xml_file.write("      <defense>"+str(pokemon1.defense)+"</defense>\n")
                continue
            if child.tag == "speed":
                xml_file.write("      <speed>"+str(pokemon1.speed)+"</speed>\n")
                continue
            if child.tag == "special":
                xml_file.write("      <special>"+str(pokemon1.special)+"</special>\n")
                xml_file.write("    </attributes>\n")
                continue
            if child.tag == "type" and j == 0:
                xml_file.write("    <type>"+pokemon1.type1 + "/" + pokemon1.type2+"</type>\n")
                j = j + 1
                continue
            if child.tag == "attacks":
                xml_file.write("    <attacks>\n")
                skill = 0
                while skill < 5:
                    if skill == 0:
                        xml_file.write("      <id>0</id>\n")
                        xml_file.write("      <name>"+pokemon1.move0.move_name+"</name>\n")
                        xml_file.write("      <type>"+pokemon1.move0.move_type+"</type>\n")
                        xml_file.write("      <power>"+str(pokemon1.move0.move_power)+"</power>\n")
                        xml_file.write("      <accuracy>"+str(pokemon1.move0.move_acc)+"</accuracy>\n")
                        xml_file.write("      <power_points>"+str(pokemon1.move0.move_pp)+"</power_points>\n")
                    if skill == 1:
                        xml_file.write("      <id>1</id>\n")
                        xml_file.write("      <name>"+pokemon1.move1.move_name+"</name>\n")
                        xml_file.write("      <type>"+pokemon1.move1.move_type+"</type>\n")
                        xml_file.write("      <power>"+str(pokemon1.move1.move_power)+"</power>\n")
                        xml_file.write("      <accuracy>"+str(pokemon1.move1.move_acc)+"</accuracy>\n")
                        xml_file.write("      <power_points>"+str(pokemon1.move1.move_pp)+"</power_points>\n")
                    if skill == 2:
                        xml_file.write("      <id>2</id>\n")
                        xml_file.write("      <name>"+pokemon1.move2.move_name+"</name>\n")
                        xml_file.write("      <type>"+pokemon1.move2.move_type+"</type>\n")
                        xml_file.write("      <power>"+str(pokemon1.move2.move_power)+"</power>\n")
                        xml_file.write("      <accuracy>"+str(pokemon1.move2.move_acc)+"</accuracy>\n")
                        xml_file.write("      <power_points>"+str(pokemon1.move2.move_pp)+"</power_points>\n")
                    if skill == 3:
                        xml_file.write("      <id>3</id>\n")
                        xml_file.write("      <name>"+pokemon1.move3.move_name+"</name>\n")
                        xml_file.write("      <type>"+pokemon1.move3.move_type+"</type>\n")
                        xml_file.write("      <power>"+str(pokemon1.move3.move_power)+"</power>\n")
                        xml_file.write("      <accuracy>"+str(pokemon1.move3.move_acc)+"</accuracy>\n")
                        xml_file.write("      <power_points>"+str(pokemon1.move3.move_pp)+"</power_points>\n")
                    if skill == 4:
                        xml_file.write("      <id>4</id>\n")
                        xml_file.write("      <name>"+pokemon1.move4.move_name+"</name>\n")
                        xml_file.write("      <type>"+pokemon1.move4.move_type+"</type>\n")
                        xml_file.write("      <power>"+str(pokemon1.move4.move_power)+"</power>\n")
                        xml_file.write("      <accuracy>"+str(pokemon1.move4.move_acc)+"</accuracy>\n")
                        xml_file.write("      <power_points>"+str(pokemon1.move4.move_pp)+"</power_points>\n")
                    skill = skill + 1
            if child.tag == "power_points":
                xml_file.write("    </attacks>\n")
                xml_file.write("  </pokemon>\n")
                k = k + 1
                i = 0
                j = 0
                continue
        #server pokemon
        else:
            if pokemon2 != None:
                if child.tag == "pokemon":
                    xml_file.write("  <pokemon>\n")
                    continue
                if child.tag == "name" and i == 0:
                    xml_file.write("    <name>"+pokemon2.name+"</name>\n")
                    i = i + 1
                    continue
                if child.tag == "level":
                    xml_file.write("    <level>"+str(pokemon2.level)+"</level>\n")
                    continue
                if child.tag == "health":
                    xml_file.write("    <attributes>\n")
                    xml_file.write("      <health>"+str(pokemon2.hp)+"</health>\n")
                    continue
                if child.tag == "attack":
                    xml_file.write("      <attack>"+str(pokemon2.attack)+"</attack>\n")
                    continue
                if child.tag == "defense":
                    xml_file.write("      <defense>"+str(pokemon2.defense)+"</defense>\n")
                    continue
                if child.tag == "speed":
                    xml_file.write("      <speed>"+str(pokemon2.speed)+"</speed>\n")
                    continue
                if child.tag == "special":
                    xml_file.write("      <special>"+str(pokemon2.special)+"</special>\n")
                    xml_file.write("    </attributes>\n")
                    continue
                if child.tag == "type" and j == 0:
                    xml_file.write("    <type>"+pokemon2.type1 + "/" + pokemon2.type2+"</type>\n")
                    j = j + 1
                    continue
                if child.tag == "attacks":
                    xml_file.write("    <attacks>\n")
                    skill = 0
                    while skill < 5:
                        if skill == 0:
                            xml_file.write("      <id>0</id>\n")
                            xml_file.write("      <name>"+pokemon2.move0.move_name+"</name>\n")
                            xml_file.write("      <type>"+pokemon2.move0.move_type+"</type>\n")
                            xml_file.write("      <power>"+str(pokemon2.move0.move_power)+"</power>\n")
                            xml_file.write("      <accuracy>"+str(pokemon2.move0.move_acc)+"</accuracy>\n")
                            xml_file.write("      <power_points>"+str(pokemon2.move0.move_pp)+"</power_points>\n")
                        if skill == 1:
                            xml_file.write("      <id>1</id>\n")
                            xml_file.write("      <name>"+pokemon2.move1.move_name+"</name>\n")
                            xml_file.write("      <type>"+pokemon2.move1.move_type+"</type>\n")
                            xml_file.write("      <power>"+str(pokemon2.move1.move_power)+"</power>\n")
                            xml_file.write("      <accuracy>"+str(pokemon2.move1.move_acc)+"</accuracy>\n")
                            xml_file.write("      <power_points>"+str(pokemon2.move1.move_pp)+"</power_points>\n")
                        if skill == 2:
                            xml_file.write("      <id>2</id>\n")
                            xml_file.write("      <name>"+pokemon2.move2.move_name+"</name>\n")
                            xml_file.write("      <type>"+pokemon2.move2.move_type+"</type>\n")
                            xml_file.write("      <power>"+str(pokemon2.move2.move_power)+"</power>\n")
                            xml_file.write("      <accuracy>"+str(pokemon2.move2.move_acc)+"</accuracy>\n")
                            xml_file.write("      <power_points>"+str(pokemon2.move2.move_pp)+"</power_points>\n")
                        if skill == 3:
                            xml_file.write("      <id>3</id>\n")
                            xml_file.write("      <name>"+pokemon2.move3.move_name+"</name>\n")
                            xml_file.write("      <type>"+pokemon2.move3.move_type+"</type>\n")
                            xml_file.write("      <power>"+str(pokemon2.move3.move_power)+"</power>\n")
                            xml_file.write("      <accuracy>"+str(pokemon2.move3.move_acc)+"</accuracy>\n")
                            xml_file.write("      <power_points>"+str(pokemon2.move3.move_pp)+"</power_points>\n")
                        if skill == 4:
                            xml_file.write("      <id>4</id>\n")
                            xml_file.write("      <name>"+pokemon2.move4.move_name+"</name>\n")
                            xml_file.write("      <type>"+pokemon2.move4.move_type+"</type>\n")
                            xml_file.write("      <power>"+str(pokemon2.move4.move_power)+"</power>\n")
                            xml_file.write("      <accuracy>"+str(pokemon2.move4.move_acc)+"</accuracy>\n")
                            xml_file.write("      <power_points>"+str(pokemon2.move4.move_pp)+"</power_points>\n")
                        skill = skill + 1
                if child.tag == "power_points":
                    xml_file.write("    </attacks>\n")
                    xml_file.write("  </pokemon>\n")
                    k = k + 1
                    i = 0
                    j = 0
    xml_file.write("</battle_state>\n")
    xml_file.close()
    xml_file = open("pokemon.xml", "r")
    xml = xml_file.read()
    return xml

def parse(xml):
    temp = open("temp.xml", "w")
    for i in xml:
        temp.write(i)
    temp.close()
    client_pokemon_parsed = False
    server_pokemon_parsed = False
    i = 0
    j = 0
    skill = 0
    tree = ElementTree.parse('temp.xml')
    root = tree.getroot()
    for child in root.iter():
        if client_pokemon_parsed == False:
            if child.tag == "name" and i == 0:
                client_pokemon_name = child.text
                i = i + 1
                continue
            if child.tag == "level":
                client_pokemon_level = int(child.text)
                continue
            if child.tag == "health":
                client_pokemon_health = int(child.text)
                continue
            if child.tag == "attack":
                client_pokemon_attack = int(child.text)
                continue
            if child.tag == "defense":
                client_pokemon_defense = int(child.text)
                continue
            if child.tag == "speed":
                client_pokemon_speed = int(child.text)
                continue
            if child.tag == "special":
                client_pokemon_special = int(child.text)
                continue
            if child.tag == "type" and j == 0:
                split_string = child.text.split('/')
                type1 = split_string[0]
                type2 = split_string[1]
                client_pokemon_type1 = type1
                client_pokemon_type2 = type2
                j = j + 1
                continue
            if child.tag == "id" and skill == 0:
                client_pokemon_move0_id = int(child.text)
                continue
            if child.tag == "name" and i == 1 and skill == 0:
                client_pokemon_move0_name = child.text
                continue
            if child.tag == "type" and j == 1 and skill == 0:
                client_pokemon_move0_type = child.text
                continue
            if child.tag == "power" and skill == 0:
                client_pokemon_move0_power = int(child.text)
                continue
            if child.tag == "accuracy" and skill == 0:
                client_pokemon_move0_accuracy = float(child.text) 
                continue
            if child.tag == "power_points" and skill == 0:
                client_pokemon_move0_power_points = int(child.text)
                skill = skill + 1
                client_pokemon_move0 = moves.create_move_dictionary(client_pokemon_move0_id, client_pokemon_move0_name, client_pokemon_move0_type, client_pokemon_move0_power_points, client_pokemon_move0_power, client_pokemon_move0_accuracy, client_pokemon_move0_power_points)
                continue
            if child.tag == "id" and skill == 1:
                client_pokemon_move1_id = int(child.text)
                continue
            if child.tag == "name" and i == 1 and skill == 1:
                client_pokemon_move1_name = child.text
                continue
            if child.tag == "type" and j == 1 and skill == 1:
                client_pokemon_move1_type = child.text
                continue
            if child.tag == "power" and skill == 1:
                client_pokemon_move1_power = int(child.text)
                continue
            if child.tag == "accuracy" and skill == 1:
                client_pokemon_move1_accuracy = float(child.text)
                continue
            if child.tag == "power_points" and skill == 1:
                client_pokemon_move1_power_points = int(child.text)
                skill = skill + 1
                client_pokemon_move1 = moves.create_move_dictionary(client_pokemon_move1_id, client_pokemon_move1_name, client_pokemon_move1_type, client_pokemon_move1_power_points, client_pokemon_move1_power, client_pokemon_move1_accuracy, client_pokemon_move1_power_points)
                continue
            if child.tag == "id" and skill == 2:
                client_pokemon_move2_id = int(child.text)
                continue
            if child.tag == "name" and i == 1 and skill == 2:
                client_pokemon_move2_name = child.text
                continue
            if child.tag == "type" and j == 1 and skill == 2:
                client_pokemon_move2_type = child.text
                continue
            if child.tag == "power" and skill == 2:
                client_pokemon_move2_power = int(child.text)
                continue
            if child.tag == "accuracy" and skill == 2:
                client_pokemon_move2_accuracy = float(child.text)
                continue
            if child.tag == "power_points" and skill == 2:
                client_pokemon_move2_power_points = int(child.text)
                skill = skill + 1
                client_pokemon_move2 = moves.create_move_dictionary(client_pokemon_move2_id, client_pokemon_move2_name, client_pokemon_move2_type, client_pokemon_move2_power_points, client_pokemon_move2_power, client_pokemon_move2_accuracy, client_pokemon_move2_power_points)
                continue
            if child.tag == "id" and skill == 3:
                client_pokemon_move3_id = int(child.text)
                continue
            if child.tag == "name" and i == 1 and skill == 3:
                client_pokemon_move3_name = child.text
                continue
            if child.tag == "type" and j == 1 and skill == 3:
                client_pokemon_move3_type = child.text
                continue
            if child.tag == "power" and skill == 3:
                client_pokemon_move3_power = int(child.text)
                continue
            if child.tag == "accuracy" and skill == 3:
                client_pokemon_move3_accuracy = float(child.text)
                continue
            if child.tag == "power_points" and skill == 3:
                client_pokemon_move3_power_points = int(child.text)
                skill = skill + 1
                client_pokemon_move3 = moves.create_move_dictionary(client_pokemon_move3_id, client_pokemon_move3_name, client_pokemon_move3_type, client_pokemon_move3_power_points, client_pokemon_move3_power, client_pokemon_move3_accuracy, client_pokemon_move3_power_points)
                continue
            if child.tag == "id" and skill == 4:
                client_pokemon_move4_id = int(child.text)
                continue
            if child.tag == "name" and i == 1 and skill == 4:
                client_pokemon_move4_name = child.text
                continue
            if child.tag == "type" and j == 1 and skill == 4:
                client_pokemon_move4_type = child.text
                continue
            if child.tag == "power" and skill == 4:
                client_pokemon_move4_power = int(child.text)
                continue
            if child.tag == "accuracy" and skill == 4:
                client_pokemon_move4_accuracy = float(child.text)
                continue
            if child.tag == "power_points" and skill == 4:
                client_pokemon_move4_power_points = int(child.text)
                skill = skill + 1
                client_pokemon_parsed = True
                client_pokemon_move4 = moves.create_move_dictionary(client_pokemon_move4_id, client_pokemon_move4_name, client_pokemon_move4_type, client_pokemon_move4_power_points, client_pokemon_move4_power, client_pokemon_move4_accuracy, client_pokemon_move4_power_points)
                i = 0
                j = 0
                skill = 0
                continue
        else: # server pokemon
            if child.tag == "name" and i == 0:
                server_pokemon_name = child.text
                print
                i = i + 1
                continue
            if child.tag == "level":
                server_pokemon_level = int(child.text)
                continue
            if child.tag == "health":
                server_pokemon_health = int(child.text)
                continue
            if child.tag == "attack":
                server_pokemon_attack = int(child.text)
                continue
            if child.tag == "defense":
                server_pokemon_defense = int(child.text)
                continue
            if child.tag == "speed":
                server_pokemon_speed = int(child.text)
                continue
            if child.tag == "special":
                server_pokemon_special = int(child.text)
                continue
            if child.tag == "type" and j == 0:
                split_string = child.text.split('/')
                type1 = split_string[0]
                type2 = split_string[1]
                server_pokemon_type1 = type1
                server_pokemon_type2 = type2
                j = j + 1
                continue
            if child.tag == "id" and skill == 0:
                server_pokemon_move0_id = int(child.text)
                continue
            if child.tag == "name" and i == 1 and skill == 0:
                server_pokemon_move0_name = child.text
                continue
            if child.tag == "type" and j == 1 and skill == 0:
                server_pokemon_move0_type = child.text
                continue
            if child.tag == "power" and skill == 0:
                server_pokemon_move0_power = int(child.text)
                continue
            if child.tag == "accuracy" and skill == 0:
                server_pokemon_move0_accuracy = float(child.text)
                continue
            if child.tag == "power_points" and skill == 0:
                server_pokemon_move0_power_points = int(child.text)
                skill = skill + 1
                server_pokemon_move0 = moves.create_move_dictionary(server_pokemon_move0_id, server_pokemon_move0_name, server_pokemon_move0_type, server_pokemon_move0_power_points, server_pokemon_move0_power, server_pokemon_move0_accuracy, server_pokemon_move0_power_points)
                continue
            if child.tag == "id" and skill == 1:
                server_pokemon_move1_id = int(child.text)
                continue
            if child.tag == "name" and i == 1 and skill == 1:
                server_pokemon_move1_name = child.text
                continue
            if child.tag == "type" and j == 1 and skill == 1:
                server_pokemon_move1_type = child.text
                continue
            if child.tag == "power" and skill == 1:
                server_pokemon_move1_power = int(child.text)
                continue
            if child.tag == "accuracy" and skill == 1:
                server_pokemon_move1_accuracy = float(child.text)
                continue
            if child.tag == "power_points" and skill == 1:
                server_pokemon_move1_power_points = int(child.text)
                skill = skill + 1
                server_pokemon_move1 = moves.create_move_dictionary(server_pokemon_move1_id, server_pokemon_move1_name, server_pokemon_move1_type, server_pokemon_move1_power_points, server_pokemon_move1_power, server_pokemon_move1_accuracy, server_pokemon_move1_power_points)
                continue
            if child.tag == "id" and skill == 2:
                server_pokemon_move2_id = int(child.text)
                continue
            if child.tag == "name" and i == 1 and skill == 2:
                server_pokemon_move2_name = child.text
                continue
            if child.tag == "type" and j == 1 and skill == 2:
                server_pokemon_move2_type = child.text
                continue
            if child.tag == "power" and skill == 2:
                server_pokemon_move2_power = int(child.text)
                continue
            if child.tag == "accuracy" and skill == 2:
                server_pokemon_move2_accuracy = float(child.text)
                continue
            if child.tag == "power_points" and skill == 2:
                server_pokemon_move2_power_points = int(child.text)
                skill = skill + 1
                server_pokemon_move2 = moves.create_move_dictionary(server_pokemon_move2_id, server_pokemon_move2_name, server_pokemon_move2_type, server_pokemon_move2_power_points, server_pokemon_move2_power, server_pokemon_move2_accuracy, server_pokemon_move2_power_points)
                continue
            if child.tag == "id" and skill == 3:
                server_pokemon_move3_id = int(child.text)
                continue
            if child.tag == "name" and i == 1 and skill == 3:
                server_pokemon_move3_name = child.text
                continue
            if child.tag == "type" and j == 1 and skill == 3:
                server_pokemon_move3_type = child.text
                continue
            if child.tag == "power" and skill == 3:
                server_pokemon_move3_power = int(child.text)
                continue
            if child.tag == "accuracy" and skill == 3:
                server_pokemon_move3_accuracy = float(child.text)
                continue
            if child.tag == "power_points" and skill == 3:
                server_pokemon_move3_power_points = int(child.text)
                skill = skill + 1
                server_pokemon_move3 = moves.create_move_dictionary(server_pokemon_move3_id, server_pokemon_move3_name, server_pokemon_move3_type, server_pokemon_move3_power_points, server_pokemon_move3_power, server_pokemon_move3_accuracy, server_pokemon_move3_power_points)
                continue
            if child.tag == "id" and skill == 4:
                server_pokemon_move4_id = int(child.text)
                continue
            if child.tag == "name" and i == 1 and skill == 4:
                server_pokemon_move4_name = child.text
                continue
            if child.tag == "type" and j == 1 and skill == 4:
                server_pokemon_move4_type = child.text
                continue
            if child.tag == "power" and skill == 4:
                server_pokemon_move4_power = int(child.text)
                continue
            if child.tag == "accuracy" and skill == 4:
                server_pokemon_move4_accuracy = float(child.text)
                continue
            if child.tag == "power_points" and skill == 4:
                server_pokemon_move4_power_points = int(child.text)
                skill = skill + 1
                server_pokemon_move4 = moves.create_move_dictionary(server_pokemon_move4_id, server_pokemon_move4_name, server_pokemon_move4_type, server_pokemon_move4_power_points, server_pokemon_move4_power, server_pokemon_move4_accuracy, server_pokemon_move4_power_points)
                server_pokemon_parsed = True
                continue
    pokemon1 = Pokemon(client_pokemon_name, client_pokemon_type1, client_pokemon_type2, client_pokemon_health, client_pokemon_level, client_pokemon_attack, client_pokemon_defense, client_pokemon_special, client_pokemon_speed, client_pokemon_move0, client_pokemon_move1, client_pokemon_move2, client_pokemon_move3, client_pokemon_move4)
    if server_pokemon_parsed == True: 
        pokemon2 = Pokemon(server_pokemon_name, server_pokemon_type1, server_pokemon_type2, server_pokemon_health, server_pokemon_level, server_pokemon_attack, server_pokemon_defense, server_pokemon_special, server_pokemon_speed, server_pokemon_move0, server_pokemon_move1, server_pokemon_move2, server_pokemon_move3, server_pokemon_move4)
    else:
        pokemon2 = None
    return pokemon1, pokemon2
