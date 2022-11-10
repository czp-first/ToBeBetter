# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之第24章
@Author  : Rey
@Time    : 2022-11-10 09:54:23
"""

from abc import ABC, abstractmethod


class Request:
    def __init__(self, request_type, request_content, number) -> None:
        self.request_type = request_type
        self.request_content = request_content
        self.number = number


class Manager(ABC):
    def __init__(self, name) -> None:
        self.name = name
        self.superior = None

    @abstractmethod
    def request_applications(self, request: Request):
        ...


class CommonManager(Manager):
    def request_applications(self, request: Request):
        if request.request_type == "请假" and request.number <= 2:
            print(f"{self.name}:{request.request_content} 数量{request.number} 被批准")
        else:
            if self.superior:
                self.superior.request_applications(request)


class Majordomo(Manager):
    def request_applications(self, request: Request):
        if request.request_type == "请假" and request.number <= 5:
            print(f"{self.name}:{request.request_content} 数量{request.number} 被批准")
        else:
            if self.superior:
                self.superior.request_applications(request)


class GeneralManager(Manager):
    def request_applications(self, request: Request):
        if request.request_type == "请假":
            print(f"{self.name}:{request.request_content} 数量{request.number} 被批准")
        elif (request.request_type == "加薪" and request.number <= 500):
            print(f"{self.name}:{request.request_content} 数量{request.number} 被批准")
        elif (request.request_type == "加薪" and request.number > 500):
            print(f"{self.name}:{request.request_content} 数量{request.number} 再说吧")


def main():
    jinli = CommonManager("金利")
    zongjian = Majordomo("宗剑")
    zhongjianli = GeneralManager("钟精励")
    jinli.superior = zongjian
    zongjian.superior = zhongjianli

    request1 = Request("请假", "小菜请假", 1)
    jinli.request_applications(request1)

    request2 = Request("请假", "小菜请假", 4)
    jinli.request_applications(request2)

    request3 = Request("加薪", "小菜请求加薪", 500)
    jinli.request_applications(request3)

    request4 = Request("加薪", "小菜请求加薪", 1000)
    jinli.request_applications(request4)


if __name__ == '__main__':
    main()
