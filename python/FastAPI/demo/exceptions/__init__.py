# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 15:21:54
"""
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException

from exceptions.not_found import NotFoundException, not_found_exception_handler
from exceptions.unprocessable_entity import UnprocessableEntityException, unprocessable_entity_exception_handler


def mount_custom_exception_handler(app: FastAPI):
    app.add_exception_handler(NotFoundException, not_found_exception_handler)
    app.add_exception_handler(UnprocessableEntityException, unprocessable_entity_exception_handler)
