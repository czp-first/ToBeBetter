# -*- coding: UTF-8 -*-
"""
@Summary : example1
@Author  : Rey
@Time    : 2022-04-28 09:42:36
"""
import xml.etree.ElementTree as etree
import json


class JSONConnector:
    def __init__(self, filepath) -> None:
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLConnector:
    def __init__(self, filepath) -> None:
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def connection_factory(filepath: str):
    if filepath.endswith('.json'):
        connector = JSONConnector
    elif filepath.endswith('.xml'):
        connector = XMLConnector
    else:
        raise ValueError(f'Cannot connect to {filepath}')
    return connector(filepath)


def connect_to(filepath):
    factory = None
    try:
        factory = connection_factory(filepath)
    except ValueError as ve:
        print(ve)
    return factory


def main():
    sqlite_factory = connect_to('data/person.sq3')
    print()

    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
    print(f'found: {len(liars)} persons')
    for liar in liars:
        print(f'first name: {liar.find("firstName").text}')
        print(f'last name: {liar.find("lastName").text}')
        [print(f'phone number ({p.attrib["type"]} {p.text})') for p in liar.find('phoneNumbers')]
    print()

    json_factory = connect_to('data/donut.json')
    json_data = json_factory.parsed_data
    print(f'found: {len(json_data)} donuts')

    for donut in json_data:
        print(f'name: {donut["name"]}')
        print(f'price: ${donut["ppu"]}')
        [print(f'topping: {t["id"]} {t["type"]}') for t in donut['topping']]


if __name__ == '__main__':
    main()
