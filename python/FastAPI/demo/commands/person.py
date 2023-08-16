# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 16:38:32
"""
from loguru import logger
from tortoise import Tortoise, run_async
import typer

from db.models.person import Person
from db.orm import TORTOISE_ORM


app = typer.Typer()


async def init_tortoise():
    await Tortoise.init(config=TORTOISE_ORM)


async def new_person(name: str, age: int):
    person = await Person.create(
        name=name,
        age=age,
    )
    logger.info("create person successfully: id[{}]", person.pk)
    return person


@app.command()
def new():
    logger.info("creating person...")
    name = input("name:")
    age = input("age:")
    if not age.isdigit():
        logger.error("age should be integer")
        typer.Exit(1)

    run_async(init_tortoise())
    run_async(new_person(name=name, age=age))
