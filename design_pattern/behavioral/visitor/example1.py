# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之第28章
@Author  : Rey
@Time    : 2022-11-10 11:30:01
"""

from abc import ABC, abstractmethod
from typing import List


class Action(ABC):
    @abstractmethod
    def get_man_conclusion(self, man):
        ...

    @abstractmethod
    def get_woman_conclusion(self, woman):
        ...


class Person(ABC):
    @abstractmethod
    def accept(self, visitor: Action):
        ...


class Man(Person):
    def accept(self, visitor: Action):
        visitor.get_man_conclusion(self)


class Woman(Person):
    def accept(self, visitor: Action):
        visitor.get_woman_conclusion(self)


class Success(Action):
    def get_man_conclusion(self, man):
        print(f"{man.__class__.__name__}{self.__class__.__name__}时, 背后多半有一个伟大的女人。")

    def get_woman_conclusion(self, woman):
        print(f"{woman.__class__.__name__}{self.__class__.__name__}时，背后大多有一个不成功的男人。")


class Failing(Action):
    def get_man_conclusion(self, man):
        print(f"{man.__class__.__name__}{self.__class__.__name__}时, 闷头喝酒，谁也不用劝。")

    def get_woman_conclusion(self, woman):
        print(f"{woman.__class__.__name__}{self.__class__.__name__}时，眼泪汪汪，谁也劝不了。")


class Amativeness(Action):
    def get_man_conclusion(self, man):
        print(f"{man.__class__.__name__}{self.__class__.__name__}时, 凡事不懂也要装懂。")

    def get_woman_conclusion(self, woman):
        print(f"{woman.__class__.__name__}{self.__class__.__name__}时，遇事懂也装作不懂。")



class ObjectStructure:
    def __init__(self) -> None:
        self.elements: List[Person] = list()

    def attach(self, element: Person):
        self.elements.append(element)

    def detach(self, element: Person):
        self.elements.remove(element)

    def display(self, visitor: Action):
        for e in self.elements:
            e.accept(visitor)


def main():
    o = ObjectStructure()
    o.attach(Man())
    o.attach(Woman())

    v1 = Success()
    o.display(v1)

    v2 = Failing()
    o.display(v2)

    v3 = Amativeness()
    o.display(v3)


if __name__ == '__main__':
    main()
