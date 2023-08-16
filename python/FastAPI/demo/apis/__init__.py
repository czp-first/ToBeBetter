# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 15:56:13
"""
from fastapi import FastAPI

from apis.endpoints import router


def init_router(app: FastAPI):
    app.include_router(router=router)
