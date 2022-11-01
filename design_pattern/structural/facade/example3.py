# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之第12章
@Author  : Rey
@Time    : 2022-10-10 13:34:34
"""

class SubSystemOne:
    def method_one(self):
        print("子系统方法一")


class SubSystemTwo:
    def method_two(self):
        print("子系统方法二")


class SubSystemThree:
    def method_three(self):
        print("子系统方法三")


class SubSystemFour:
    def method_four(self):
        print("子系统方法四")


class Facade:
    def __init__(self) -> None:
        self.one = SubSystemOne()
        self.two = SubSystemTwo()
        self.three = SubSystemThree()
        self.four = SubSystemFour()

    def method_a(self):
        print("方法组A()")
        self.one.method_one()
        self.two.method_two()
        self.four.method_four()

    def method_b(self):
        print("方法组B()")
        self.two.method_two()
        self.three.method_three()


def main():
    facade = Facade()
    facade.method_a()
    facade.method_b()


if __name__ == '__main__':
    main()
