# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式第6章
@Author  : Rey
@Time    : 2022-10-09 14:02:02
"""

from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def show(self):
        ...


class Person(Component):
    def __init__(self, name=None) -> None:
        self._name = name

    def show(self):
        print(f"装扮的{self._name}")


class Finery(Person):
    def decorate(self, component: Person):
        self._component = component

    def show(self):
        if self._component:
            self._component.show()


class TShirts(Finery):
    def show(self):
        print("大T恤", end=" ")
        return super().show()


class BigTrouser(Finery):
    def show(self):
        print("垮裤", end=" ")
        return super().show()


def main():
    xc = Person("小菜")
    print("第一种装扮: ")

    kk = BigTrouser()
    dtx = TShirts()

    kk.decorate(xc)
    dtx.decorate(kk)
    dtx.show()


if __name__ == '__main__':
    main()
