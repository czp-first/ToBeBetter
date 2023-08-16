# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 15:25:09
"""
from pathlib import Path

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from settings import get_settings


def get_orm_models():
    models = []
    db_path = Path(__file__).parent / "models"

    for child in db_path.iterdir():
        if child.is_file() and not child.name.startswith("__") and not child.name.startswith("."):
            models.append(f"db.models.{child.stem}")
    return models


pg_settings = get_settings(key="pg")

TORTOISE_ORM = {
    "connections": {
        "default": str(pg_settings.dsn),
    },
    "apps": {
        "models": {"models": get_orm_models(), "default_connection": "default"},
    },
    "use_tz": False,
    "timezone": "Asia/Shanghai",
}


generate_schemas = False


def switch_to_test_mode():
    global TORTOISE_ORM, generate_schemas
    TORTOISE_ORM["connections"]["default"] = "sqlite://:memory:"
    generate_schemas = True


def init(app: FastAPI):
    register_tortoise(
        app,
        TORTOISE_ORM,
        add_exception_handlers=True,
        generate_schemas=generate_schemas,
    )
