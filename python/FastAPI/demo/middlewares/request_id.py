# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 15:14:08
"""
from uuid import uuid4

from fastapi.requests import Request
from loguru import logger


async def add_request_id_dispatch(request: Request, call_next):
    request_uuid = str(uuid4())
    request["headers"].append((b"x-request-id", request_uuid.encode()))
    x_forwarded_for = request.headers.get("x_forwarded_for", "127.0.0.1")
    login_ip = x_forwarded_for.split(",")[0] if x_forwarded_for and x_forwarded_for.split(",") else ""
    logger.info(
        "[{}]:from[{}],method[{}],url[{}],base_url[{}],path[{}],path_params[{}], query_params[{}]",
        request_uuid, login_ip, request.method, request.url, request.base_url, request.url.path, request.path_params, request.query_params
    )
    return await call_next(request)
