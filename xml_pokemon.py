#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.etree import ElementTree
from pokemon import Pokemon


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
                    continue
                if child.tag == "name" and i == 0:
                    i = i + 1
                    continue
                if child.tag == "level":
                    continue
                if child.tag == "health":
                    continue
                if child.tag == "attack":
                    continue
                if child.tag == "defense":
                    continue
                if child.tag == "speed":
                    continue
                if child.tag == "special":
                    continue
                if child.tag == "type" and j == 0:
                    j = j + 1
                    continue
                if child.tag == "id":
                    continue
                if child.tag == "name" and i == 1:
                    continue
                if child.tag == "type" and j == 1:
                    continue
                if child.tag == "power":
                    continue
                if child.tag == "accuracy":
                    continue
                if child.tag == "power_points":
                    continue
    xml_file.write("</battle_state>\n")
    xml_file.close()
    xml_file = open("pokemon.xml", "r")
    xml = xml_file.read()
    return xml


def parse(xml):
    parsed_xml = ElementTree.fromstring(xml)
    pokemon1 = Pokemon(parsed_xml)
    pokemon2 = Pokemon(parsed_xml)
    return pokemon1, pokemon2
