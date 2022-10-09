# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之第7章
@Author  : Rey
@Time    : 2022-10-09 16:48:59
"""

from abc import ABC, abstractmethod


class SchoolGirl:
    def __init__(self, name) -> None:
        self.name = name


class GiveGift(ABC):
    @abstractmethod
    def give_dolls(self):
        ...

    @abstractmethod
    def give_flowers(self):
        ...

    @abstractmethod
    def give_chocolate(self):
        ...


class Pursuit(GiveGift):
    def __init__(self, mm: SchoolGirl) -> None:
        super().__init__()
        self.mm = mm

    def give_dolls(self):
        print(f"{self.mm.name}送你洋娃娃")

    def give_flowers(self):
        print(f"{self.mm.name}送你鲜花")

    def give_chocolate(self):
        print(f"{self.mm.name}送你巧克力")


class Proxy(GiveGift):
    def __init__(self, mm: SchoolGirl) -> None:
        self.gg = Pursuit(mm)

    def give_dolls(self):
        self.gg.give_dolls()

    def give_flowers(self):
        self.gg.give_flowers()

    def give_chocolate(self):
        self.gg.give_chocolate()
