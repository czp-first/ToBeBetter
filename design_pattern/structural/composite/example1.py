# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之第19章
@Author  : Rey
@Time    : 2022-11-02 09:34:04
"""

from abc import ABC, abstractmethod
from typing import List


class Company(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def add(self, company):
        ...

    @abstractmethod
    def remove(self, company):
        ...

    @abstractmethod
    def display(self, depth: int):
        ...

    @abstractmethod
    def line_of_duty(self):
        ...


class ConcreteCompany(Company):
    def __init__(self, name) -> None:
        super().__init__(name)
        self.children: List[Company] = []

    def add(self, company):
        self.children.append(company)

    def remove(self, company):
        self.children.remove(company)

    def display(self, depth: int):
        print("-"*depth, self.name)

        for component in self.children:
            component.display(depth+2)

    def line_of_duty(self):
        for component in self.children:
            component.line_of_duty()


class HRDepartment(Company):

    def add(self, company):
        return

    def remove(self, company):
        return

    def display(self, depth: int):
        print("-"*depth, self.name)

    def line_of_duty(self):
        print(f"{self.name} 员工招聘培训管理")


class FinanceDepartment(Company):
    def add(self, company):
        return

    def remove(self, company):
        return

    def display(self, depth: int):
        print("-"*depth, self.name)

    def line_of_duty(self):
        print(f"{self.name} 公司财务收支管理")


if __name__ == '__main__':
    root = ConcreteCompany("北京总公司")
    root.add(HRDepartment("总公司人力资源部"))
    root.add(FinanceDepartment("总公司财务部"))

    comp = ConcreteCompany("上海华东分公司")
    comp.add(HRDepartment("华东分公司人力资源部"))
    comp.add(FinanceDepartment("华东分公司财务部"))
    root.add(comp)

    comp1 = ConcreteCompany("南京办事处")
    comp1.add(HRDepartment("南京办事处人力资源部"))
    comp1.add(FinanceDepartment("南京办事处财务部"))
    comp.add(comp1)

    comp2 = ConcreteCompany("杭州办事处")
    comp2.add(HRDepartment("杭州办事处人力资源部"))
    comp2.add(FinanceDepartment("杭州办事处财务部"))
    comp.add(comp2)

    print("结构图:")
    root.display(1)

    print("职责:")
    root.line_of_duty()
