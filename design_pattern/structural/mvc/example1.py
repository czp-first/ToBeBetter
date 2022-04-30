# -*- coding: UTF-8 -*-
"""
@Summary : example1 of mvc1
@Author  : Rey
@Time    : 2022-04-30 17:46:10
"""


quotes = (
    'A man is not complete until he is married. Then he is finished.',
    'As I said before, I never repeat myself.',
    'Black holes really suck...',
    'Facts are stubborn things.',
)


class QuoteModel:
    def get_quote(self, n):
        try:
            value = quotes[n]
        except IndexError:
            value = 'Not found!'
        return value


class QuoteTerminalView:
    def show(self, quote):
        print(f'And the quote is: {quote}')

    def error(self, msg):
        print(f'Error: {msg}')

    def select_quote(self):
        return input('Which quote number would you like to see?')


class QuoteTerminalController:
    def __init__(self) -> None:
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            try:
                n = self.view.select_quote()
                n = int(n)
                valid_input = True
            except ValueError:
                self.view.error(f'Incorrect index "{n}"')
        quote = self.model.get_quote(n)
        self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == '__main__':
    main()
