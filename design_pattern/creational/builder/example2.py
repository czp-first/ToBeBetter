# -*- coding: UTF-8 -*-
"""
@Summary : example2 of builder
@Author  : Rey
@Time    : 2022-04-29 19:35:25
"""

class Pizza:
    def __init__(self, builder) -> None:
        self.garlic = builder.garlic
        self.extra_cheese = builder.extra_cheese

    def __str__(self) -> str:
        garlic = 'yes' if self.garlic else 'no'
        cheese = 'yes' if self.extra_cheese else 'no'
        info = (f'Garlic: {garlic}', f'Extra cheese: {cheese}')
        return '\n'.join(info)

    class PizzaBuilder:
        def __init__(self) -> None:
            self.extra_cheese = False
            self.garlic = False

        def add_garlic(self):
            self.garlic = True
            return self

        def add_extra_cheese(self):
            self.extra_cheese = True
            return self

        def build(self):
            return Pizza(self)


if __name__ == '__main__':
    pizza = Pizza.PizzaBuilder().add_garlic().add_extra_cheese().build()
    print(pizza)
