"""
user routes
"""

from fastapi import APIRouter, Depends, Path
from fastapi import status
from typing import Annotated, List
from app.security.get_user import get_user_from_token
from app.models.user import Users
from app.schemas.user import UserDetails
from beanie.operators import In


""" initialize the router """
router = APIRouter(prefix="/user", tags=["User"])


@router.get(
    "/details",
    summary="Get User Details",
    status_code=status.HTTP_200_OK,
    response_model=UserDetails,
)
async def get_user_info(user: Annotated[Users, Depends(get_user_from_token)]):
    """View the user information of the logged in user"""
    return user


@router.get(
    "/referred-singups/{page}",
    summary="List Of Users Signed Up With My Referral Code",
    status_code=status.HTTP_200_OK,
    response_model=List[UserDetails],
)
async def get_all_user_signups(
    user: Annotated[Users, Depends(get_user_from_token)],
    page: Annotated[int, Path(title="Page", gt=0)],
):
    """
    get the authenticated user from the token
    extract the users that registered with this users
    referral. then get the data of every user from db
    """
    limit = 20
    skip = (page - 1) * limit
    all_users = (
        await Users.find(In(Users.id, user.referral_signup))
        .skip(skip)
        .limit(limit)
        .to_list()
    )

    return all_users
