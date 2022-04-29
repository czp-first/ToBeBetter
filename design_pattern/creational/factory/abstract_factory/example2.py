# -*- coding: UTF-8 -*-
"""
@Summary : abstract factory example2
@Author  : Rey
@Time    : 2022-04-28 11:22:16
"""
import random
from typing import Type


class Pet:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class Dog(Pet):
    def speak(self) -> None:
        print('woof')

    def __str__(self) -> str:
        return f'Dog<{self.name}>'


class Cat(Pet):
    def speak(self) -> None:
        print('meow')

    def __str__(self) -> str:
        return f'Cat<{self.name}>'


class PetShop:
    def __init__(self, animal_factory: Type[Pet]) -> None:
        self.pet_factory = animal_factory

    def buy_pet(self, name: str) -> Pet:
        pet = self.pet_factory(name)
        print(f'Here is your lovely {pet}')
        return pet


def random_animal(name: str) -> Pet:
    return random.choice([Dog, Cat])(name)


def main() -> None:
    """
    >>> cat_shop = PetShop(Cat)
    >>> pet = cat_shop.buy_pet('Lucy')
    Here is your lovely Cat<Lucy>
    >>> pet.speak()
    meow

    >>> shop = PetShop(random_animal)
    >>> for name in ['Max', 'Jack', 'Buddy']:
    ...     pet = shop.buy_pet(name)
    ...     pet.speak()
    ...     print('=' * 20)
    Here is your lovely Cat<Max>
    meow
    ====================
    Here is your lovely Dog<Jack>
    woof
    ====================
    Here is your lovely Dog<Buddy>
    woof
    ====================
    """


if __name__ == '__main__':
    random.seed(1234)
    import doctest

    doctest.testmod()
