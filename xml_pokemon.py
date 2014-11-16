#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.etree import ElementTree
from pokemon import Pokemon


def generate(pokemon1, pokemon2 = None):
	tree = ElementTree.parse('structure.xml')
	root = tree.getroot()
	xml_file = open('pokemon.xml', 'w')
	print("AQUI1 " + str(tree))
	print("AQUI2 " + str(root))
	print("AQUI3 ")
	i = 0
	j = 0
	k = 0
	for child in root.iter():
		print(child.tag,"-->", child.attrib)
		#pokemon do cliente
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
			if child.tag == "id":
				xml_file.write("    <attacks>\n")
				xml_file.write("      <id>NotSelectedYet</id>\n")
				continue
			if child.tag == "name" and i == 1:
				xml_file.write("      <name>NotSelectedYet</name>\n")
				continue
			if child.tag == "type" and j == 1:
				xml_file.write("      <type>NotSelectedYet</type>\n")
				continue
			if child.tag == "power":
				xml_file.write("      <power>NotSelectedYet</power>\n")
				continue
			if child.tag == "accuracy":
				xml_file.write("      <accuracy>NotSelectedYet</accuracy>\n")
				continue
			if child.tag == "power_points":
				xml_file.write("      <power_points>NotSelectedYet</power_points>\n")
				xml_file.write("    </attacks>\n")
				xml_file.write("  </pokemon>\n")
				k = k + 1
				i = 0
				j = 0
				continue
		#pokemon do servidor
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

	print(xml)
	#DEBUG
	#for child in root.iter():
	#	print(child.tag,"-->", child.attrib)
	return xml


def parse(xml):
    parsed_xml = ElementTree.fromstring(xml)
    pokemon1 = Pokemon(parsed_xml)
    pokemon2 = Pokemon(parsed_xml)
    return pokemon1, pokemon2




#	tree = ElementTree.parse('pokemon.xml')
#	root = tree.getroot()
#	print("AQUI1 " + str(tree))
#	print("AQUI2 " + str(root))
#	print("AQUI3 ")
#	for name in root.iter('{http://www.w3.org/2001/XMLSchema}element'):
#		print(name.attrib)
#		for key, value in name.attrib.items():
#			print(key, "->", value)
#	return xml