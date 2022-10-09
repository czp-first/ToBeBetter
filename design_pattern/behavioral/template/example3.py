# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之第10章
@Author  : Rey
@Time    : 2022-10-09 18:13:35
"""

from abc import ABC, abstractproperty

class TestPaper(ABC):
    def test_question1(self):
        print("屠龙刀的玄铁可能是[]")
        print(f"答案:{self.answer1}")

    def test_question2(self):
        print("铲除了情花，造成了[]")
        print(f"答案是:{self.answer2}")

    @abstractproperty
    def answer1(self):
        ...

    @abstractproperty
    def answer2(self):
        ...


class TestPaperA(TestPaper):
    @property
    def answer1(self):
        return "b"

    @property
    def answer2(self):
        return "c"


class TestPaperB(TestPaper):
    @property
    def answer1(self):
        return "c"

    @property
    def answer2(self):
        return "a"


def main():
    student_a = TestPaperA()
    student_a.test_question1()
    student_a.test_question2()

    student_b = TestPaperB()
    student_b.test_question1()
    student_b.test_question2()


if __name__ == '__main__':
    main()
