# -*- coding: UTF-8 -*-
"""
@Summary : example2 of decorator
@Author  : Rey
@Time    : 2022-04-30 16:02:14
"""


class TextTag:
    def __init__(self, text) -> None:
        self._text = text

    def render(self):
        return self._text


class BoldWrapper(TextTag):
    def __init__(self, wrapped) -> None:
        self._wrapped = wrapped

    def render(self):
        return f'<b>{self._wrapped.render()}</b>'


class ItalicWrapper(TextTag):
    def __init__(self, wrapped) -> None:
        self._wrapped = wrapped

    def render(self):
        return f'<i>{self._wrapped.render()}</i>'


def main():
    """
    >>> simple_hello = TextTag("hello, world!")
    >>> special_hello = ItalicWrapper(BoldWrapper(simple_hello))

    >>> print('before:', simple_hello.render())
    before: hello, world!

    >>> print('after:', special_hello.render())
    after: <i><b>hello, world!</b></i>
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
