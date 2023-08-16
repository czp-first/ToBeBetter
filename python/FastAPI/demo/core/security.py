# -*- coding: UTF-8 -*-
"""
@Summary : docstr
@Author  : Rey
@Time    : 2023-08-16 16:39:41
"""
import base64
from datetime import timedelta
from hashlib import sha1, sha256
import hmac
import json
import random
import string

from cryptography.fernet import Fernet, InvalidToken
from pydantic import BaseModel, ValidationError
from tortoise.timezone import now

from exceptions.unauthorized import UnAuthorizedException


DEFAULT_DECODE = "UTF-8"


def gen_hashed_password(password: str, password_salt: str) -> str:
    """
    哈希密码
    :param password: 密码
    :param password_salt: 盐
    :return:
    """
    salted_sha1 = sha1((password + password_salt).encode())
    hashed_base64 = base64.b64encode(salted_sha1.digest()).decode(DEFAULT_DECODE)
    return hashed_base64


def gen_random_string(length: int):
    """
    生成指定长度的随机字符串
    :param length: 长度
    :return:
    """
    return "".join(random.sample(string.ascii_letters + string.digits, length))


class Token(BaseModel):
    access_key: str
    exp: int


class Auth:
    def __init__(self, secret: str) -> None:
        # self._secret = secret
        self._f = Fernet(key=secret.encode("utf-8"))

    def encrypt(self, access_key: str, expire_seconds: int):
        exp = (now() + timedelta(seconds=expire_seconds)).timestamp()
        token = Token(
            access_key=access_key,
            exp=exp,
        )
        return self._f.encrypt(data=token.model_dump_json().encode("utf-8")).decode("utf-8")

    def decrypt(self, token: str):
        try:
            decrypted_token = self._f.decrypt(data=token)
        except (InvalidToken, ValidationError):
            raise UnAuthorizedException
        return Token.model_validate(decrypted_token)


def sign(secret: str, data: dict):
    # sorted_keys = sorted(data.keys())
    # msg_list = [f'"{key}":"{data[key]}"' for key in sorted_keys]
    # msg = ",".join(msg_list)
    # msg = "{" + msg + "}"
    msg = json.dumps(data)
    msg_bytes = msg.encode("utf-8")
    secret_bytes = secret.encode("utf-8")
    sign_bytes = base64.b64encode(hmac.new(key=secret_bytes, msg=msg_bytes, digestmod=sha256).digest())

    return sign_bytes.decode("utf-8")
