# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 16:13:01
"""
from pydantic import BaseModel


class PersonResp(BaseModel):
    id: int
    name: str
    age: int
