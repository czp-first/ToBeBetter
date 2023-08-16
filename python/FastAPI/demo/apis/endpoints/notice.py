# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 16:25:19
"""
from fastapi import APIRouter, Body, Header
from fastapi.background import BackgroundTasks

from apis.schemas.base import CommonResp
from apis.schemas.notice import NoticeBody
from tasks.notice import send_msg

notice_router = APIRouter(prefix="/notices")


@notice_router.post("")
async def notice(background_tasks: BackgroundTasks, body: NoticeBody = Body(...), x_request_id: str = Header(None)):
    background_tasks.add_task(func=send_msg, request_id=x_request_id, title=body.title, content=body.content)
    return CommonResp()
