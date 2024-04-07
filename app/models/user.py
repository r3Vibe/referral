""" user model """

from beanie import Document, Indexed
from typing import Annotated, List
from pydantic import Field
from datetime import datetime
from uuid import UUID, uuid4
from app.utils.referral_generator import create_ref_code


class Users(Document):
    id: UUID = Field(default_factory=uuid4)
    name: str
    email: Annotated[str, Indexed(unique=True)]
    password: str
    referral_code: str = Field(default_factory=create_ref_code)
    points: int = Field(default=0)
    referral_signup: List[UUID] = Field(default=[])
    createdAt: datetime = Field(default_factory=datetime.now)

    class Settings:
        name = "users"
