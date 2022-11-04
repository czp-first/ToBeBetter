# -*- coding: UTF-8 -*-
"""
@Summary : https://sourcemaking.com/design_patterns/singleton/python/1
@Author  : Rey
@Time    : 2022-11-04 15:36:05
"""

class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class MyClass(metaclass=Singleton):
    pass


def main():
    m1 = MyClass()
    m2 = MyClass()
    assert m1 is m2


if __name__ == '__main__':
    main()
