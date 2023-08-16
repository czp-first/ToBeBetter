# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 16:41:51
"""
from enum import Enum

from fastapi import status
from fastapi.responses import JSONResponse
from loguru import logger

from exceptions.base import DemoHttpException


class UnAuthEnum(Enum):
    """401"""
    INVALID_CREDENTIALS = "invalid_credentials"


class UnAuthorizedException(DemoHttpException):
    """401异常类"""

    def __init__(self, code: UnAuthEnum = UnAuthEnum.INVALID_CREDENTIALS):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, code=code
        )


def unauthorized_exception_handler(request, exc: UnAuthorizedException):
    """
    401异常类的handler
    :param request: 请求
    :param exc: 异常
    :return:
    """
    logger.warning("[{}]: raise UnAuthorizedException code[{}] value[{}]", request.headers.get("x-request-id"), exc.status_code, exc.code.value)
    return JSONResponse(
        content={"code": exc.status_code, "msg": exc.code.value, "data": None},
        status_code=status.HTTP_200_OK
    )
