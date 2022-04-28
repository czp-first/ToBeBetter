# -*- coding: UTF-8 -*-
"""
@Summary : example2
@Author  : Rey
@Time    : 2022-04-28 10:13:09
"""
class ChineseLocalizer:
    def __init__(self) -> None:
        self.translations = {'dog': '狗', 'cat': '猫'}

    def localize(self, msg: str) -> str:
        return self.translations.get(msg, msg)


class EnglishLocalizer:
    def localize(self, msg: str) -> str:
        return msg


def get_localizer(language: str = 'English') -> object:
    localizers = {
        'Chinese': ChineseLocalizer,
        'English': EnglishLocalizer,
    }
    return localizers[language]()


def main():
    """
    # Create localizers
    >>> e, g = get_localizer(language='English'), get_localizer(language='Chinese')

    >>> for msg in 'dog parrot cat bear'.split():
    ...     print(e.localize(msg), g.localize(msg))
    dog 狗
    parrot parrot
    cat 猫
    bear bear
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
