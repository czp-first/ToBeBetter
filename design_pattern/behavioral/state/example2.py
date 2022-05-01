# -*- coding: UTF-8 -*-
"""
@Summary : example2 of state
@Author  : Rey
@Time    : 2022-05-01 18:36:39
"""


class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print(f'Scanning... Station is {self.stations[self.pos]} {self.name}')


class AmState(State):
    def __init__(self, radio) -> None:
        super().__init__()
        self.radio = radio
        self.stations = ['1250', '1380', '1510']
        self.pos = 0
        self.name = 'AM'

    def toggle_amfm(self):
        print(f'Switching to FM')
        self.radio.state = self.radio.fmstate


class FmState(State):
    def __init__(self, radio) -> None:
        super().__init__()
        self.radio = radio
        self.stations = ['81.3', '89.1', '103.9']
        self.pos = 0
        self.name ='FM'

    def toggle_amfm(self):
        print('Switching to AM')
        self.radio.state = self.radio.amstate


class Radio:
    def __init__(self) -> None:
        self.amstate = AmState(self)
        self.fmstate = FmState(self)
        self.state = self.amstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()


def main():
    """
    >>> radio = Radio()
    >>> actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
    >>> actions *= 2

    >>> for action in actions:
    ...     action()
    Scanning... Station is 1380 AM
    Scanning... Station is 1510 AM
    Switching to FM
    Scanning... Station is 89.1 FM
    Scanning... Station is 103.9 FM
    Scanning... Station is 81.3 FM
    Scanning... Station is 89.1 FM
    Switching to AM
    Scanning... Station is 1250 AM
    Scanning... Station is 1380 AM
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
