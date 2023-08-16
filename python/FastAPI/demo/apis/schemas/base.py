# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 16:01:11
"""
from typing import Dict, Union

from fastapi import status
from pydantic import BaseModel, Field


class CommonResp(BaseModel):
    code: int = Field(default=status.HTTP_200_OK)
    msg: str = Field(default="")
    data: Union[BaseModel, Dict] = {}
