""" get the user from the token """

from app.models.user import Users
from fastapi import HTTPException, status, Depends
from typing import Annotated
from app.security.jwt_bearer import JwtBearer
from app.security.jwt import verify_token
from uuid import UUID


async def get_user_from_token(
        token: Annotated[str, Depends(JwtBearer())]) -> Users:
    """
    jwtbearer will return the token if it is valid.
    we will take the token and extract the user from their
    """
    payload = verify_token(token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token Expired"
        )

    user = await Users.find_one(Users.id == UUID(payload["id"]))

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Does Not Exists"
        )

    return user
