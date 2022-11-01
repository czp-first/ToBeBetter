# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之第17章
@Author  : Rey
@Time    : 2022-11-01 17:53:29
"""

from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def attack(self):
        ...

    @abstractmethod
    def defense(self):
        ...


class Forward(Player):
    def attack(self):
        print(f"前锋{self.name}进攻")

    def defense(self):
        print(f"前锋{self.name}防守")


class Center(Player):
    def attack(self):
        print(f"中锋{self.name}进攻")

    def defense(self):
        print(f"中锋{self.name}防守")


class Guard(Player):
    def attack(self):
        print(f"后卫{self.name}进攻")

    def defense(self):
        print(f"后卫{self.name}防守")


class ForeignCenter:
    def __init__(self, name) -> None:
        self.name = name

    def 进攻(self):
        print(f"外籍中锋{self.name}进攻")

    def 防守(self):
        print(f"外籍中锋{self.name}防守")


class Translator(Player):
    def __init__(self, name) -> None:
        self.wjzf = ForeignCenter(name)

    def attack(self):
        self.wjzf.进攻()

    def defense(self):
        self.wjzf.防守()


if __name__ == '__main__':
    b = Forward("巴蒂尔")
    b.attack()

    m = Guard("麦迪")
    m.attack()

    ym = Translator("姚明")
    ym.attack()
    ym.defense()
