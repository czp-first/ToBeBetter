# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 15:09:03
"""
from fastapi import FastAPI
import sentry_sdk

from apis import init_router
from apis.schemas.base import CommonResp
from core.events import create_start_app_handler, create_stop_app_handler
from db.orm import init as init_orm
from exceptions import mount_custom_exception_handler
from init_logger import init_logger
from middlewares import mount_middlewares
from settings import get_settings


def create_app():
    sentry_settings = get_settings(key="sentry")
    if sentry_settings.is_enable:
        sentry_sdk.init(
            dsn=sentry_settings.dsn,
            traces_sample_rate=1.0,
            environment=sentry_settings.environment,
        )

    log_settings = get_settings(key="log")
    init_logger(file=log_settings.file)

    version = "0.0.1"
    app = FastAPI(title="demo", version=version)
    init_orm(app=app)

    app.add_event_handler(event_type="startup", func=create_start_app_handler(app=app))
    app.add_event_handler(event_type="shutdown", func=create_stop_app_handler(app=app))

    mount_custom_exception_handler(app=app)
    mount_middlewares(app=app)

    init_router(app=app)
    return app


app = create_app()


@app.get("/")
def index():
    return CommonResp(msg="demo")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
