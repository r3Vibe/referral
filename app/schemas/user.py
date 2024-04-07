""" user scehma for request and response """

from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from fastapi import Body


class UserSchema(BaseModel):
    name: str = Body(title="Name of the user")
    email: EmailStr = Body(title="Valid Email Address")
    password: str = Body(title="Secure Password")
    referral_code: Optional[str] = Body(
        default=None,
        title="Referral Code Given By Someone",
    )


class UserRegistrationResponse(BaseModel):
    id: UUID
    message: str = "User Registration Successful"


class LoginSchema(BaseModel):
    email: EmailStr = Body(title="Email Address")
    password: str = Body(title="Password")


class UserDetails(BaseModel):
    name: str
    email: EmailStr
    referral_code: str
    createdAt: datetime
