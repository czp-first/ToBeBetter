# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 16:30:04
"""
from loguru import logger


async def send_msg(request_id: str, title: str, content: str):
    logger.info("[{}]: title[{}], content[{}]", request_id, title, content)
