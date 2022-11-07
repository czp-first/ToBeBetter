# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之第22章
@Author  : Rey
@Time    : 2022-11-07 17:33:36
"""

from abc import ABC, abstractmethod


class HandsetSoft(ABC):
    @abstractmethod
    def run(self):
        ...


class HandsetGame(HandsetSoft):
    def run(self):
        print("运行手机游戏")


class HandsetAddressList(HandsetSoft):
    def run(self):
        print("运行手机通讯录")


class HandsetBrand(ABC):

    def set_soft(self, soft: HandsetSoft):
        self.soft = soft

    @abstractmethod
    def run(self):
        ...


class HandsetBrandN(HandsetBrand):
    def run(self):
        self.soft.run()


class HandsetBrandM(HandsetBrand):
    def run(self):
        self.soft.run()


if __name__ == '__main__':
    ab = HandsetBrandN()

    ab.set_soft(HandsetGame())
    ab.run()

    ab.set_soft(HandsetAddressList())
    ab.run()

    ab = HandsetBrandM()

    ab.set_soft(HandsetGame())
    ab.run()

    ab.set_soft(HandsetAddressList())
    ab.run()
