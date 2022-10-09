# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之第九章
@Author  : Rey
@Time    : 2022-10-09 17:27:34
"""

from abc import ABC, abstractmethod
import copy


class Cloneable(ABC):
    @abstractmethod
    def clone(self):
        ...


class WorkExperience(Cloneable):
    def __init__(self, work_date, company) -> None:
        self.work_date = work_date
        self.company = company

    def clone(self):
        return copy.copy(self)


class Resume(Cloneable):
    def __init__(self, name: str = None, work: WorkExperience = None) -> None:
        self.name = name
        if work:
            self.work = work.clone()
        else:
            self.work = work
        self.work = work

    def set_personal_info(self, sex, age):
        self.sex = sex
        self.age = age

    def set_work_experience(self, work_date, company):
        if not self.work:
            self.work = WorkExperience(work_date, company)
        else:
            self.work.work_date = work_date
            self.work.company = company

    def display(self):
        print(f"{self.name}, {self.sex}, {self.age}")
        print(f"工作经历: {self.work.work_date} {self.work.company}")

    def clone(self):
        obj = Resume(self.work)
        obj.name = self.name
        obj.sex = self.sex
        obj.age = self.age
        return obj


def main():
    a = Resume("大鸟")
    a.set_personal_info("男", "29")
    a.set_work_experience("1998-2000", "XX公司")

    b = a.clone()
    b.set_work_experience("1998-2006", "YY企业")

    c = a.clone()
    c.set_work_experience("1998-2003", "ZZ企业")

    a.display()
    b.display()
    c.display()


if __name__ == '__main__':
    main()
