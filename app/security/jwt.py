""" handle json web token logic here """

from jose import jwt, JWTError
from app.config.settings import settings
import time


def make_token(id: str) -> str:
    """create new jwt token and return it"""
    return jwt.encode(
        {"id": id, "expiry": time.time() + 600}, settings.SECRET, "HS256")


def verify_token(tok: str) -> bool:
    """verify the given token for validity"""
    try:
        data = jwt.decode(tok, settings.SECRET, algorithms=["HS256"])
        return data if data["expiry"] >= time.time() else None
    except JWTError:
        return None
