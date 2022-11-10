# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之地25章
@Author  : Rey
@Time    : 2022-11-10 10:20:21
"""

from abc import ABC, abstractmethod


class UnitedNations(ABC):
    @abstractmethod
    def declare(self, message, colleague):
        ...


class Country(ABC):
    def __init__(self, mediator) -> None:
        self.mediator = mediator


class USA(Country):
    def declare(self, message):
        self.mediator.declare(message, self)

    def get_message(self, message):
        print("美国获得对方消息: ", message)


class Iraq(Country):
    def declare(self, message):
        self.mediator.declare(message, self)

    def get_message(self, message):
        print("伊拉克获得对方信息: ", message)


class UnitedNationsSecurityCouncil(UnitedNations):
    def __init__(self) -> None:
        self.colleague1 = None
        self.colleague2 = None

    def declare(self, message, colleague):
        if colleague == self.colleague1:
            self.colleague2.get_message(message)
        else:
            self.colleague1.get_message(message)


def main():
    unsc = UnitedNationsSecurityCouncil()
    c1 = USA(unsc)
    c2 = Iraq(unsc)

    unsc.colleague1 = c1
    unsc.colleague2 = c2

    c1.declare("不准研制核武器, 否则要发动战争!")
    c2.declare("我们没有核武器, 也不怕侵略。")


if __name__ == '__main__':
    main()
