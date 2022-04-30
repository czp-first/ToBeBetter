# -*- coding: UTF-8 -*-
"""
@Summary : example2 of adapter
@Author  : Rey
@Time    : 2022-04-30 15:14:41
"""

from typing import Callable, TypeVar

T = TypeVar('T')


class Dog:
    def __init__(self) -> None:
        self.name = 'Dog'

    def bark(self) -> str:
        return 'woof!'


class Cat:
    def __init__(self) -> None:
        self.name = 'Cat'

    def meow(self) -> str:
        return 'meow!'


class Human:
    def __init__(self) -> None:
        self.name = 'Human'

    def speak(self) -> str:
        return "'hello'"


class Car:
    def __init__(self) -> None:
        self.name = 'Car'

    def make_noise(self, octane_level: int) -> str:
        return f'vroom{"!" * octane_level}'


class Adapter:
    def __init__(self, obj: T, **adapted_methods: Callable) -> None:
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__


def main():
    """
    >>> objects = []
    >>> dog = Dog()
    >>> print(dog.__dict__)
    {'name': 'Dog'}

    >>> objects.append(Adapter(dog, make_noise=dog.bark))

    >>> # objects[0].__dict__['obj'], objects[0].__dict__['make_noise']
    >>> # (<...Dog object at 0x...>, <bound method Dog.bark of <...Dog object at 0x...>>)

    >>> print(objects[0].original_dict())
    {'name': 'Dog'}

    >>> cat = Cat()
    >>> objects.append(Adapter(cat, make_noise=cat.meow))
    >>> human = Human()
    >>> objects.append(Adapter(human, make_noise=human.speak))
    >>> car = Car()
    >>> objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))

    >>> for obj in objects:
    ...     print("A {0} goes {1}".format(obj.name, obj.make_noise()))
    A Dog goes woof!
    A Cat goes meow!
    A Human goes 'hello'
    A Car goes vroom!!!
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
