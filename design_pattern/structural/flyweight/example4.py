# -*- coding: UTF-8 -*-
"""
@Summary : 大话设计模式之第26章
@Author  : Rey
@Time    : 2022-11-10 10:56:12
"""

from abc import ABC, abstractmethod


class User:
    def __init__(self, name) -> None:
        self.name = name


class Website(ABC):
    @abstractmethod
    def use(self, user: User):
        ...


class ConcreteWebsite(Website):
    def __init__(self, name) -> None:
        self.name = name

    def use(self, user: User):
        print(f"网站分类: {self.name}, 用户: {user.name}")


class WebsiteFactory:
    def __init__(self) -> None:
        self.flyweights = dict()

    def get_website_category(self, key) -> Website:
        if key not in self.flyweights:
            self.flyweights[key] = ConcreteWebsite(key)
        return self.flyweights[key]

    def get_website_count(self):
        return len(self.flyweights)


def main():
    f = WebsiteFactory()

    fx = f.get_website_category("产品展示")
    fx.use(User("小菜"))

    fy = f.get_website_category("产品展示")
    fy.use(User("大鸟"))

    fz = f.get_website_category("产品展示")
    fz.use(User("娇娇"))

    fl = f.get_website_category("博客")
    fl.use(User("老顽童"))

    fm = f.get_website_category("博客")
    fm.use(User("桃谷六仙"))

    fn = f.get_website_category("博客")
    fn.use(User("南海鳄神"))

    print(f"得到网站分类总数为{f.get_website_count()}")


if __name__ == '__main__':
    main()
