""" given a string it will be converted to a secure hash """

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """hash and return the given password string"""
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    """check given password against the password hash"""
    return pwd_context.verify(password, hashed)
