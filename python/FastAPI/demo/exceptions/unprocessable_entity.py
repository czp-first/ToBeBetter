# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 15:20:50
"""
from enum import Enum

from fastapi import status
from fastapi.logger import logger
from fastapi.responses import JSONResponse

from exceptions.base import DemoHttpException


class UnprocessableEntityEnum(Enum):
    """422"""
    UNPROCESSABLE_ENTITY = "UNPROCESSABLE_ENTITY"


class UnprocessableEntityException(DemoHttpException):
    """422异常类"""

    def __init__(self, code=UnprocessableEntityEnum.UNPROCESSABLE_ENTITY):
        super(UnprocessableEntityException, self).__init__(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            code=code,
        )


def unprocessable_entity_exception_handler(request, exc: DemoHttpException):
    """
    422异常类的handler
    :param request: 请求
    :param exc: 异常
    :return:
    """
    logger.warning("[{}]: raise UnprocessableEntityException code[{}] value[{}]", request.headers.get("x-request-id"), exc.status_code, exc.code.value)
    return JSONResponse(
        content={"code": exc.status_code, "msg": exc.code.value, "data": None},
        status_code=exc.status_code
    )
