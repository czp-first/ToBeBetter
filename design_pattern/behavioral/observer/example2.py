# -*- coding: UTF-8 -*-
"""
@Summary : example2 of observer
@Author  : Rey
@Time    : 2022-05-01 17:39:21
"""

from __future__ import annotations

from contextlib import suppress
from typing import Protocol


class Observer(Protocol):
    def update(self, subject: Subject) -> None:
        pass


class Subject:
    def __init__(self) -> None:
        self._observers = list[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        with suppress(ValueError):
            self._observers.remove(observer)

    def notify(self, modifier: Observer | None = None) -> None:
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)


class Data(Subject):
    def __init__(self, name: str = '') -> None:
        super().__init__()
        self.name = name
        self._data = 0

    @property
    def data(self) -> int:
        return self._data

    @data.setter
    def data(self, value) -> None:
        self._data = value
        self.notify()


class HexViewer:
    def update(self, subject: Data) -> None:
        print(f'HexViewer: Subject {subject.name} has data 0x{subject.data:x}')


class DecimalViewer:
    def update(self, subject: Data) -> None:
        print(f'DecimalViewer: Subject {subject.name} has data {subject.data}')


def main():
    """
    >>> data1 = Data('Data 1')
    >>> data2 = Data('Data 2')
    >>> view1 = DecimalViewer()
    >>> view2 = HexViewer()
    >>> data1.attach(view1)
    >>> data1.attach(view2)
    >>> data2.attach(view2)
    >>> data2.attach(view1)

    >>> data1.data = 10
    DecimalViewer: Subject Data 1 has data 10
    HexViewer: Subject Data 1 has data 0xa

    >>> data2.data = 15
    HexViewer: Subject Data 2 has data 0xf
    DecimalViewer: Subject Data 2 has data 15

    >>> data1.data = 3
    DecimalViewer: Subject Data 1 has data 3
    HexViewer: Subject Data 1 has data 0x3

    >>> data2.data = 5
    HexViewer: Subject Data 2 has data 0x5
    DecimalViewer: Subject Data 2 has data 5

    >>> data1.detach(view2)
    >>> data2.detach(view2)

    >>> data1.data = 10
    DecimalViewer: Subject Data 1 has data 10

    >>> data2.data = 15
    DecimalViewer: Subject Data 2 has data 15
    """


if __name__ == '__main__':
    main()
