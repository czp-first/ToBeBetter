# -*- coding: UTF-8 -*-
"""
@Summary : example2 of command
@Author  : Rey
@Time    : 2022-05-01 16:27:39
"""

from typing import List, Union


class HideFileCommand:
    def __init__(self) -> None:
        self._hidden_files: List[str] = []

    def execute(self, filename: str) -> None:
        print(f'hiding {filename}')
        self._hidden_files.append(filename)

    def undo(self) -> None:
        filename = self._hidden_files.pop()
        print(f'un-hiding {filename}')


class DeleteFileCommand:
    def __init__(self) -> None:
        self._deleted_files: List[str] = []

    def execute(self, filename: str) -> None:
        print(f'deleting {filename}')
        self._deleted_files.append(filename)

    def undo(self) -> None:
        filename = self._deleted_files.pop()
        print(f'restoring {filename}')


class MenuItem:
    def __init__(self, command: Union[HideFileCommand, DeleteFileCommand]) -> None:
        self._command = command

    def on_do_press(self, filename: str) -> None:
        self._command.execute(filename)

    def on_undo_press(self) -> None:
        self._command.undo()


def main():
    """
    >>> item1 = MenuItem(DeleteFileCommand())

    >>> item2 = MenuItem(HideFileCommand())

    >>> test_file_name = 'test-file'

    >>> item1.on_do_press(test_file_name)
    deleting test-file

    >>> item1.on_undo_press()
    restoring test-file

    >>> item2.on_do_press(test_file_name)
    hiding test-file

    >>> item2.on_undo_press()
    un-hiding test-file
    """


if __name__ == '__main__':
    import doctest

    doctest.testmod()
