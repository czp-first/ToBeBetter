# -*- coding: UTF-8 -*-
"""
@Summary : example1 of adapter
@Author  : Rey
@Time    : 2022-04-30 15:07:29
"""

class Synthesizer:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f'the {self.name} synthesizer'

    def play(self):
        return 'is playing an electronic song'


class Human:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f'{self.name} the human'

    def speak(self):
        return 'says hello'


class Computer:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f'the {self.name} computer'

    def execute(self):
        return 'executes a program'


class Adapter:
    def __init__(self, obj, adapted_methods) -> None:
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self) -> str:
        return str(self.obj)


def main():
    objects = [Computer('Asus')]
    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human('Bob')
    objects.append(Adapter(human, dict(execute=human.speak)))

    for i in objects:
        print(f'{str(i)} {i.execute()}')


if __name__ == '__main__':
    main()
