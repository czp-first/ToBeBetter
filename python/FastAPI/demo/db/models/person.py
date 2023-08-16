# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 15:27:54
"""
from tortoise import fields

from db.models.base import DatetimeModel


class Person(DatetimeModel):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=64)
    age = fields.IntField()

    class Meta:
        table = "person"
        description = "persion"
