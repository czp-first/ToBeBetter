# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之第1章
@Author  : Rey
@Time    : 2022-10-09 11:14:41
"""

from abc import ABC, abstractproperty


class Operation(ABC):
    def __init__(self, number1, number2) -> None:
        self.number1 = number1
        self.numer2 = number2

    @abstractproperty
    def result(self):
        ...


class OperationAdd(Operation):
    @property
    def result(self):
        return self.number1 + self.numer2


class OperationSub(Operation):
    @property
    def result(self):
        return self.number1 - self.numer2


class OperationMul(Operation):
    @property
    def result(self):
        return self.number1 * self.numer2


class OperationDiv(Operation):
    @property
    def result(self):
        if self.numer2 == 0:
            raise ValueError("divisor cant be zero")
        return self.number1 / self.numer2


def operation_factory(operate):
    if operate == "+":
        return OperationAdd
    elif operate == "-":
        return OperationSub
    elif operate == "*":
        return OperationMul
    elif operate == "/":
        return OperationDiv
    else:
        raise TypeError("invalid operate")


def operation_instance(operate, number1, number2):
    oper = operation_factory(operate)
    return oper(number1, number2)


def main():
    add = operation_instance("+", 1, 2)
    assert add.result == 3

    sub = operation_instance("-", 1, 2)
    assert sub.result == -1

    mul = operation_instance("*", 2, 3)
    assert mul.result == 6

    div = operation_instance("/", 4, 2)
    assert div.result == 2


if __name__ == '__main__':
    main()
