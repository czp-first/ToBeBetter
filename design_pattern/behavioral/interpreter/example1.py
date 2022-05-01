# -*- coding: UTF-8 -*-
"""
@Summary : exampl1 of interpreter
@Author  : Rey
@Time    : 2022-05-01 16:53:31
"""

from pyparsing import Word, OneOrMore, Optional, Group, Suppress, alphanums


class Gate:
    def __init__(self) -> None:
        self.is_open = False

    def __str__(self) -> str:
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the gate')
        self.is_open = True

    def close(self):
        print('closing the gate')
        self.is_open = False


class Garage:
    def __init__(self) -> None:
        self.is_open = False

    def __str__(self) -> str:
        return 'open' if self.is_open else 'closed'

    def open(self):
        print('opening the garage')
        self.is_open = True

    def close(self):
        print('closing the garage')
        self.is_open = False


class Aircondition:
    def __init__(self) -> None:
        self.is_on = False

    def __str__(self) -> str:
        return 'on' if self.is_on else 'off'

    def turn_on(self):
        print('turning on the aircondition')
        self.is_on = True

    def turn_off(self):
        print('turing off the aircondition')
        self.is_on = False


class Heating:
    def __init__(self) -> None:
        self.is_on = False

    def __str__(self) -> str:
        return 'on' if self.is_on else 'off'

    def turn_on(self):
        print('turning on the heating')
        self.is_on = True

    def turn_off(self):
        print('turing off the heating')
        self.is_on = False


class Boiler:
    def __init__(self):
        self.temperature = 83

    def __str__(self) -> str:
        return f'boiler temperature: {self.temperature}'

    def increase_temperature(self, amount):
        print(f'increasing the boiler\'s temperature by {amount} degree')

    def decrease_temperature(self, amount):
        print(f'decreasing the boiler\'s temperature by {amount} degree')


class Fridge:
    def __init__(self) -> None:
        self.temperature = 2

    def __str__(self) -> str:
        return f'fridge temperature: {self.temperature}'

    def increase_temperature(self, amount):
        print(f'increasing the fridge\'s temperature by {amount} degree')

    def decrease_temperature(self, amount):
        print(f'decreasing the fridge\'s temperature by {amount} degree')


def main():
    word = Word(alphanums)
    command = Group(OneOrMore(word))
    token = Suppress('->')
    device = Group(OneOrMore(word))
    argument = Group(OneOrMore(word))
    event = command + token + device + Optional(token+argument)

    gate = Gate()
    garage = Garage()
    airco = Aircondition()
    heating = Heating()
    boiler = Boiler()
    fridge = Fridge()

    tests = (
        'open -> gate',
        'close -> garage',
        'turn on -> aircondition',
        'turn off -> heating',
        'increase -> boiler temperature -> 5 degrees',
        'decrease -> fridge temperature -> 2 degrees',
    )

    open_actions = {
        'gate': gate.open,
        'garage': garage.open,
        'aircondition': airco.turn_on,
        'heating': heating.turn_on,
        'boiler temperature': boiler.increase_temperature,
        'fridge temperature': fridge.increase_temperature,
    }

    close_actions = {
        'gate': gate.close,
        'garage': garage.open,
        'aircondition': airco.turn_off,
        'heating': heating.turn_off,
        'boiler temperature': boiler.decrease_temperature,
        'fridge temperature': boiler.decrease_temperature,
    }

    for t in tests:
        if len(event.parse_string(t)) == 2:
            cmd, dev = event.parse_string(t)
            cmd_str, dev_str = ' '.join(cmd), ' '.join(dev)
            if 'open' in cmd_str or 'turn on' in cmd_str:
                open_actions[dev_str]()
            elif 'close' in cmd_str or 'turn off' in cmd_str:
                close_actions[dev_str]()
        elif len(event.parse_string(t)) == 3:
            cmd, dev, arg = event.parse_string(t)
            cmd_str, dev_str, arg_str = ' '.join(cmd), ' '.join(dev), ' '.join(arg)
            num_arg = 0
            try:
                num_arg = int(arg_str.split()[0])
            except ValueError:
                print(f'expected number but got: "{arg_str[0]}"')
            if 'increase' in cmd_str and num_arg > 0:
                open_actions[dev_str](num_arg)
            elif 'decrease' in cmd_str and num_arg > 0:
                close_actions[dev_str](num_arg)


if __name__ == '__main__':
    main()
