# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之第2章
@Author  : Rey
@Time    : 2022-10-09 11:54:53
"""

from abc import ABC, abstractmethod
from decimal import Decimal
import math


class Strategy(ABC):
    @abstractmethod
    def accept_cash(self, money: Decimal) -> Decimal:
        ...


class CashNormal(Strategy):
    def accept_cash(self, money: Decimal) -> Decimal:
        return money


class CashRebate(Strategy):
    def __init__(self, rebate: Decimal = Decimal("0.2")) -> None:
        self._rebate = rebate

    def accept_cash(self, money: Decimal) -> Decimal:
        return money * self._rebate


class CashReturn(Strategy):
    def __init__(self, condition: Decimal = Decimal("0.0"), retu: Decimal = Decimal("0.0")) -> None:
        self._condition = condition
        self._retu = retu

    def accept_cash(self, money: Decimal) -> Decimal:
        result = money
        if (money >= self._condition):
            result = money - math.floor(money / self._condition) * self._retu
        return result


class CashContext:
    def __init__(self, strategy_type: str) -> None:
        self._strategy = None
        if strategy_type == "正常收费":
            self._strategy = CashNormal()
        elif strategy_type == "满300返100":
            self._strategy = CashReturn(Decimal("300"), Decimal("100"))
        elif strategy_type == "打8折":
            self._strategy = CashRebate(Decimal("0.8"))
        else:
            raise TypeError("invalid strategy type")

    def get_result(self, money):
        return self._strategy.accept_cash(money)


def main():
    normal = CashContext("正常收费")
    assert normal.get_result(Decimal(100)) == Decimal("100")

    retu = CashContext("满300返100")
    assert retu.get_result(Decimal("300")) == Decimal("200")

    rebate = CashContext("打8折")
    assert rebate.get_result(Decimal("100")) == Decimal("80")


if __name__ == '__main__':
    main()
