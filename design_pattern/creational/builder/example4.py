# -*- coding: UTF-8 -*-
"""
@Summary :大话设计模式之第13章
@Author  : Rey
@Time    : 2022-10-10 14:07:53
"""

from abc import ABC, abstractmethod


class Product:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def show(self):
        for part in self.parts:
            print(part)


class Builder(ABC):
    @abstractmethod
    def build_part_a(self):
        ...

    @abstractmethod
    def build_part_b(self):
        ...

    @abstractmethod
    def get_result(self) -> Product:
        ...


class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        self.product = Product()

    def build_part_a(self):
        self.product.parts.append("部件A")

    def build_part_b(self):
        self.product.parts.append("部件B")

    def get_result(self) -> Product:
        return self.product


class ConcreteBuilder2(Builder):
    def __init__(self) -> None:
        self.product = Product()

    def build_part_a(self):
        self.product.parts.append("部件X")

    def build_part_b(self):
        self.product.parts.append("部件Y")

    def get_result(self) -> Product:
        return self.product


class Director:
    def construct(self, builder: Builder):
        builder.build_part_a()
        builder.build_part_b()


def main():
    director = Director()
    b1 = ConcreteBuilder1()
    b2 = ConcreteBuilder2()

    director.construct(b1)
    p1 = b1.get_result()
    p1.show()

    director.construct(b2)
    p2 = b2.get_result()
    p2.show()


if __name__ == '__main__':
    main()
