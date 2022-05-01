# -*- coding: UTF-8 -*-
"""
@Summary : example1 of observer
@Author  : Rey
@Time    : 2022-05-01 17:28:33
"""


class Publisher:
    def __init__(self) -> None:
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print(f'Failed to add: {observer}')

    def remove(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print(f'Failed to remove: {observer}')

    def notify(self):
        [o.notify(self) for o in self.observers]


class DefaultFormatter(Publisher):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self._data = 0

    def __str__(self) -> str:
        return f'{type(self).__name__}: "{self.name}" has data = {self._data}'

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as err:
            print(f'Error: {err}')
        else:
            self.notify()


class HexFormatter:
    def notify(self, publisher):
        return f'{type(self).__name__}: "{publisher.name}" has now hex data = {hex(publisher.data)}'


class BinaryFormatter:
    def notify(self, publisher):
        return f'{type(self).__name__}: "{publisher.name}" has now bin data = {bin(publisher.data)}'


def main():
    df = DefaultFormatter('test1')
    print(df)

    print()
    hf = HexFormatter()
    df.add(hf)
    df.data = 3
    print(df)

    print()
    bf = BinaryFormatter()
    df.add(bf)
    df.data = 21
    print(df)

    print()
    df.remove(hf)
    df.data = 40
    print(df)

    print()
    df.remove(hf)
    df.add(bf)

    df.data = 'hello'
    print(df)

    print()
    df.data = 15.8
    print(df)


if __name__ == '__main__':
    main()
