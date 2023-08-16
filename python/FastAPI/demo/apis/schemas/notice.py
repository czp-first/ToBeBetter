# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 16:27:03
"""
from pydantic import BaseModel


class NoticeBody(BaseModel):
    title: str
    content: str
