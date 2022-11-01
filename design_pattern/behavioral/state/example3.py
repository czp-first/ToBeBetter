# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之第16章
@Author  : Rey
@Time    : 2022-11-01 16:28:50
"""

from abc import ABC, abstractmethod


class Work:
    def __init__(self) -> None:
        self.current: State = ForenoonState()
        self.hour = 0
        self.finish = False

    def finish_task(self):
        self.finish = True

    def write_program(self):
        self.current.write_program(self)


class State(ABC):
    @abstractmethod
    def write_program(self, w: Work):
        pass


class ForenoonState(State):
    def write_program(self, w: Work):
        if w.hour < 12:
            print(f"当前时间: {w.hour}点 上午工作, 精神百倍")
        else:
            w.current = NoonState()
            w.write_program()


class NoonState(State):
    def write_program(self, w: Work):
        if w.hour < 13:
            print(f"当前时间: {w.hour}点 饿了, 午饭: 犯困, 午休。")
        else:
            w.current = AfternoonState()
            w.write_program()


class AfternoonState(State):
    def write_program(self, w: Work):
        if w.hour < 17:
            print(f"当前时间: {w.hour}点 下午状态还不错, 继续努力")
        else:
            w.current = EveningState()
            w.write_program()


class EveningState(State):
    def write_program(self, w: Work):
        if w.finish:
            w.current = RestState()
            w.write_program()
        else:
            if w.hour < 21:
                print(f"当前时间: {w.hour}点加班哦, 疲累之极。")
            else:
                w.current = SleepingState()
                w.write_program()


class SleepingState(State):
    def write_program(self, w: Work):
        print(f"当前时间: {w.hour}点不行了, 睡着了。")


class RestState(State):
    def write_program(self, w: Work):
        print(f"当前时间: {w.hour}点下班回家了")


if __name__ == '__main__':
    emergency_project = Work()
    emergency_project.hour = 9
    emergency_project.write_program()
    emergency_project.hour = 10
    emergency_project.write_program()
    emergency_project.hour = 12
    emergency_project.write_program()
    emergency_project.hour = 13
    emergency_project.write_program()
    emergency_project.hour = 14
    emergency_project.write_program()
    emergency_project.hour = 17
    emergency_project.write_program()

    # emergency_project.finish = True
    emergency_project.finish = False

    emergency_project.write_program()
    emergency_project.hour = 19
    emergency_project.write_program()
    emergency_project.hour = 22
    emergency_project.write_program()
