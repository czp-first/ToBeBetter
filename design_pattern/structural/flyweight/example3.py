# -*- coding: UTF-8 -*-
"""
@Summary : example3 of flyweight
@Author  : Rey
@Time    : 2022-04-30 17:10:08
"""

import weakref


class FlyweightMeta(type):
    def __new__(mcs, name, parents, dct):
        dct['pool'] = weakref.WeakValueDictionary()
        return super().__new__(mcs, name, parents, dct)

    @staticmethod
    def _serializer_params(cls, *args, **kwargs):
        args_list = list(map(str, args))
        args_list.extend([str(kwargs), cls.__name__])
        key = ''.join(args_list)
        return key

    def __call__(cls, *args, **kwargs):
        key = FlyweightMeta._serializer_params(cls, *args, **kwargs)
        pool = getattr(cls, 'pool', {})

        instance = pool.get(key)
        if instance is None:
            instance = super().__call__(*args, **kwargs)
            pool[key] = instance
        return instance


class Card(metaclass=FlyweightMeta):
    def __init__(self, *args, **kwargs) -> None:
        pass


if __name__ == '__main__':
    instance_pool = getattr(Card, 'pool')
    cm1 = Card('10', 'h', a=1)
    cm2 = Card('10', 'h', a=1)
    cm3 = Card('10', 'h', a=2)

    assert (cm1 == cm2) and (cm1 != cm3)
    assert (cm1 is cm2) and (cm1 is not cm3)
    assert len(instance_pool) == 2

    del cm1
    assert len(instance_pool) == 2

    del cm2
    assert len(instance_pool) == 1

    del cm3
    assert len(instance_pool) == 0
