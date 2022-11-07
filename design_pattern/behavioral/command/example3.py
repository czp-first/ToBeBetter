# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之第23章
@Author  : Rey
@Time    : 2022-11-07 17:54:40
"""

from abc import ABC, abstractmethod


class Receiver:
    def action(self):
        print("执行请求!")


class Command(ABC):
    def __init__(self, receiver: Receiver) -> None:
        self.receiver = receiver

    @abstractmethod
    def execute(self):
        ...


class ConcreteCommand(Command):
    def execute(self):
        self.receiver.action()


class Invoker:
    def set_command(self, command: Command):
        self.command = command

    def execute(self):
        self.command.execute()


if __name__ == '__main__':
    receiver = Receiver()
    command = ConcreteCommand(receiver)
    invoker = Invoker()
    invoker.set_command(command)
    invoker.execute()
