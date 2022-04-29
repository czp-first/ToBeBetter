# -*- coding: UTF-8 -*-
"""
@Summary : abstract method example1
@Author  : Rey
@Time    : 2022-04-28 10:25:21
"""
class Frog:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle):
        print(f'{self} the Fog encounters {obstacle} and {obstacle.action()}!')


class Bug:
    def __str__(self) -> str:
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld:
    def __init__(self, name) -> None:
        print(self)
        self.player_name = name

    def __str__(self) -> str:
        return '\n\n\t------ Frog World ------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizzard:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle):
        print(f'{self} the Wizard battles against {obstacle} and {obstacle.action()}!')


class Ork:
    def __str__(self) -> str:
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizzardWorld:
    def __init__(self, name) -> None:
        print(self)
        self.player_name = name

    def __str__(self) -> str:
        return '\n\n\t------ Wizzard World ------'

    def make_character(self):
        return Wizzard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnvironment:
    def __init__(self, factory) -> None:
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input(f'Welcome {name}. How old are you?')
        age = int(age)
    except ValueError:
        print(f'Age {age} is invalid, please try again...')
        return (False, age)
    return (True, age)


def main():
    name = input("Hello. What's your name?")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizzardWorld
    environment = GameEnvironment(game(name))
    environment.play()


if __name__ == '__main__':
    main()
