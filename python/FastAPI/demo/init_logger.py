# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 15:44:56
"""
from loguru import logger


def init_logger(file):
    logger.add(file, backtrace=True, rotation="500 MB")
