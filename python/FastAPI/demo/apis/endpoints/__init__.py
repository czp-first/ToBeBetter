# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 15:56:46
"""
from fastapi.routing import APIRouter

from apis.endpoints.person import person_router
from apis.endpoints.notice import notice_router


router = APIRouter(prefix="/api")

router.include_router(router=person_router)
router.include_router(router=notice_router)
