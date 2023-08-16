# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 16:46:14
"""
from loguru import logger
import typer

from core.security import gen_hashed_password, gen_random_string


app = typer.Typer()


@app.command()
def new():
    logger.info("creating user...")
    access_key = gen_random_string(length=10)
    access_key_salt = gen_random_string(length=10)
    hashed_access_key = gen_hashed_password(password=access_key, password_salt=access_key_salt)
    logger.info("access token: {}", hashed_access_key)

    secret = gen_random_string(length=10)
    secret_salt = gen_random_string(length=10)
    hashed_secret = gen_hashed_password(password=secret, password_salt=secret_salt)
    logger.info("secret: {}", hashed_secret)
