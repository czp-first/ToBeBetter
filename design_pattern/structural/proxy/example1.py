# -*- coding: UTF-8 -*-
"""
@Summary : example1 of proxy
@Author  : Rey
@Time    : 2022-04-30 18:37:03
"""


class LazyProperty:
    def __init__(self, method) -> None:
        self.method = method
        self.method_name = method.__name__

    def __get__(self, obj, cls):
        if not obj:
            return None
        value = self.method(obj)
        setattr(obj, self.method_name, value)
        return value


class Test:
    def __init__(self) -> None:
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        print(f'initializing self._resource which is: {self._resource}')
        self._resource = tuple(range(5))
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)

    print(t.resource)
    print(t.resource)


if __name__ == '__main__':
    main()
