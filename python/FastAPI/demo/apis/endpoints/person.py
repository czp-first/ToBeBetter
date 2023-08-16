# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 15:29:51
"""
from fastapi import APIRouter, Header, Path
from loguru import logger

from apis.schemas.person import PersonResp
from db.models.person import Person
from exceptions.not_found import NotFoundEnum, NotFoundException


person_router = APIRouter(prefix="/persons")


@person_router.get("/{person_id}")
async def get_person(person_id: int = Path(...)):
    person = await Person.get_or_none(pk=person_id)
    if not person:
        raise NotFoundException(code=NotFoundEnum.PERSON)

    return PersonResp(
        id=person.pk,
        name=person.name,
        age=person.age,
    )
