# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 15:19:14
"""
from enum import Enum

from fastapi import status
from fastapi.responses import JSONResponse
from loguru import logger

from exceptions.base import DemoHttpException


class NotFoundEnum(Enum):
    """404"""
    NOT_FOUND = "NOT_FOUND"
    PERSON = "NO_PERSON"


class NotFoundException(DemoHttpException):
    """404异常类"""

    def __init__(self, code=NotFoundEnum.NOT_FOUND):
        super(NotFoundException, self).__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            code=code,
        )


def not_found_exception_handler(request, exc: DemoHttpException):
    """
    404异常类的handler
    :param request: 请求
    :param exc: 异常
    :return:
    """
    logger.warning("[{}]: raise NotFoundException code[{}] value[{}]", request.headers.get("x-request-id"), exc.status_code, exc.code.value)
    return JSONResponse(
        content={"code": exc.status_code, "msg": exc.code.value, "data": None},
        status_code=exc.status_code,
    )
