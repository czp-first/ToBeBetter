# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 16:47:54
"""
import typer

from commands.person import app as person_app
from commands.user import app as user_app


app = typer.Typer()


app.add_typer(typer_instance=person_app, name="person")
app.add_typer(typer_instance=user_app, name="user")


if __name__ == '__main__':
    app()
