# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 15:12:22
"""
from functools import lru_cache

from loguru import logger
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class EnvironmentSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file="envs/environment.env")

    environment: str = "local"


class LogSettings(BaseSettings):
    file: str


class PgSettings(BaseSettings):
    host: str
    port: int = 5432
    user: str
    password: str
    db: str

    @property
    def dsn(self):
        return PostgresDsn.build(
            scheme="postgres",
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            path=self.db,
        )


class SentrySettings(BaseSettings):
    is_enable: bool = False
    dsn: str = ""
    environment: str = "dev"


@lru_cache()
def get_settings(key):
    environment = EnvironmentSettings().environment
    logger.info("environment: {}", environment)
    dotenvfile = f"envs/{environment}.env"
    if key == "pg":
        return PgSettings(_env_file=dotenvfile, _env_prefix="pg_")
    elif key == "log":
        return LogSettings(_env_file=dotenvfile, _env_prefix="log_")
    elif key == "sentry":
        return SentrySettings(_env_file=dotenvfile, _env_prefix="sentry_")
