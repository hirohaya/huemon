#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.etree import ElementTree
from pokemon import Pokemon

def generate(pokemon1, pokemon2 = None):
    xml = ""
    return xml


def parse(xml):
    parsed_xml = ElementTree.fromstring(xml)
    pokemon1 = Pokemon(parsed_xml)
    pokemon2 = Pokemon(parsed_xml)
    return pokemon1, pokemon2