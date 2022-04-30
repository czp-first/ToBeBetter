# -*- coding: UTF-8 -*-
"""
@Summary : example2 of prototype
@Author  : Rey
@Time    : 2022-04-30 13:56:30
"""
from __future__ import annotations

from typing import Any


class Prototype:
    def __init__(self, value: str = 'default', **attrs: Any)-> None:
        self.value = value
        self.__dict__.update(attrs)

    def clone(self, **attrs: Any) -> Prototype:
        # copy.deepcopy can be used instead of next line
        obj = self.__class__(**self.__dict__)
        obj.__dict__.update(attrs)
        return obj


class PrototypeDispatcher:
    def __init__(self) -> None:
        self._objects = {}

    def get_objects(self) -> dict[str, Prototype]:
        return self._objects

    def register_object(self, name: str, obj: Prototype) -> None:
        self._objects[name] = obj

    def unregister_object(self, name: str) -> None:
        del self._objects[name]


def main():
    """
    >>> dispatcher = PrototypeDispatcher()
    >>> prototype = Prototype()

    >>> d = prototype.clone()
    >>> a = prototype.clone(value='a-value', category='a')
    >>> b = a.clone(value='b-value', is_checked=True)
    >>> dispatcher.register_object('objecta', a)
    >>> dispatcher.register_object('objectb', b)
    >>> dispatcher.register_object('default', d)

    >>> [{n: p.value} for n, p in dispatcher.get_objects().items()]
    [{'objecta': 'a-value'}, {'objectb': 'b-value'}, {'default': 'default'}]

    >>> print(b.category, b.is_checked)
    a True
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
