# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 15:18:14
"""

class DemoException(Exception):
    pass


class DemoHttpException(DemoException):
    def __init__(self, status_code, code) -> None:
        self._status_code = status_code
        self._code = code

    @property
    def status_code(self):
        return self._status_code

    @property
    def code(self):
        return self._code

    def __str__(self) -> str:
        return f"status_code={self._status_code}, code={self._code}"
