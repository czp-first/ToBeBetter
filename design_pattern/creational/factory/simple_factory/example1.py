# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之第8章
@Author  : Rey
@Time    : 2022-10-09 17:08:00
"""

from abc import ABC, abstractmethod


class LeiFeng:
    def sweep(self):
        print("扫地")

    def wash(self):
        print("洗衣")

    def buy_rice(self):
        print("买大米")


class Undergraduate(LeiFeng):
    pass


class Volunteer(LeiFeng):
    pass


class LeifengFactory(ABC):
    @abstractmethod
    def create_lei_feng(self):
        ...


class UndergraduateFactory(LeifengFactory):
    def create_lei_feng(self):
        return Undergraduate()


class VolunteerFactory(LeifengFactory):
    def create_lei_feng(self):
        return Volunteer()


def main():
    factory = UndergraduateFactory()
    leifeng = factory.create_lei_feng()
    leifeng.sweep()
    leifeng.wash()
    leifeng.buy_rice()


if __name__ == '__main__':
    main()
