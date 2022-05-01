# -*- coding: UTF-8 -*-
"""
@Summary : example2 of chain of responsibility
@Author  : Rey
@Time    : 2022-05-01 15:26:20
"""

from abc import ABC, abstractmethod
from typing import Optional, Tuple


class Handler(ABC):
    def __init__(self, successor: Optional['Handler'] = None) -> None:
        self.successor = successor

    def handle(self, request: int) -> None:
        res = self.check_range(request)
        if not res and self.successor:
            self.successor.handle(request)

    @abstractmethod
    def check_range(self, request: int) -> Optional[bool]:
        pass


class ConcreteHandler0(Handler):
    def check_range(self, request: int) -> Optional[bool]:
        if 0 <= request < 10:
            print(f'request {request} handled in handler 0')
            return True
        return None


class ConcreteHandler1(Handler):
    start, end = 10, 20

    def check_range(self, request: int) -> Optional[bool]:
        if self.start <= request < self.end:
            print(f'request {request} handled in handler 1')
            return True
        return None


class ConcreteHandler2(Handler):
    def check_range(self, request: int) -> Optional[bool]:
        start, end = self.get_interval_from_db()
        if start <= request < end:
            print(f'request {request} handled in handler 2')
            return True
        return None

    @staticmethod
    def get_interval_from_db() -> Tuple[int, int]:
        return 20, 30


class FallbackHandler(Handler):
    @staticmethod
    def check_range(request: int) -> Optional[bool]:
        print(f'end of chain, no handler for {request}')
        return False


def main():
    """
    >>> h0 = ConcreteHandler0()
    >>> h1 = ConcreteHandler1()
    >>> h2 = ConcreteHandler2(FallbackHandler())
    >>> h0.successor = h1
    >>> h1.successor = h2

    >>> requests = [2, 5, 14, 22, 18, 3, 35, 27, 20]
    >>> for request in requests:
    ...     h0.handle(request)
    request 2 handled in handler 0
    request 5 handled in handler 0
    request 14 handled in handler 1
    request 22 handled in handler 2
    request 18 handled in handler 1
    request 3 handled in handler 0
    end of chain, no handler for 35
    request 27 handled in handler 2
    request 20 handled in handler 2
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
