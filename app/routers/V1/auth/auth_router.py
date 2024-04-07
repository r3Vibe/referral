"""
auth routes file
all the auth related routes will
be defined here
"""

from fastapi import APIRouter, HTTPException
from app.schemas.user import LoginSchema, UserRegistrationResponse, UserSchema
from fastapi import status
from app.models.user import Users
from pymongo.errors import OperationFailure, DuplicateKeyError
from app.security import password as password_helper
from app.security.jwt import make_token


""" initialize the router """
router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register",
    summary="Create New Users Given Their Details",
    status_code=status.HTTP_201_CREATED,
    response_model=UserRegistrationResponse,
    responses={
        400: {
            "content": {
                "application/json": {
                    "example": {"detail": "User already exists"}}
            },
        },
        500: {
            "content": {
                "application/json": {
                    "example": {"detail": "Unable to add user"}}
            },
        },
    },
)
async def register_new_user(user: UserSchema):
    """Endpoint to register new users"""
    try:
        # get the respons in a dict
        request_data = user.model_dump()

        # get referral_code out of the request
        referral_code = request_data.pop("referral_code", None)
        password = request_data.pop("password", None)

        # create new user object
        new_user = Users(
            **request_data, password=password_helper.hash_password(password)
        )

        # save the user to db
        await new_user.insert()

        # we will find the user and update their points
        if referral_code is not None:
            ref_user = await Users.find_one(
                Users.referral_code == referral_code)
            if ref_user:
                ref_user.points = ref_user.points + 1
                ref_user.referral_signup.append(new_user.id)
                await ref_user.save()

        # return the new user object
        return new_user
    except DuplicateKeyError:
        # raise exception if user already exists
        raise HTTPException(
            status_code=400,
            detail="User already exists",
        )
    except OperationFailure:
        # raise exception if could not create entry
        raise HTTPException(
            status_code=500,
            detail="Unable to add user",
        )


@router.post("/login", summary="Login Users and return token")
async def login(user_data: LoginSchema):
    request_data = user_data.model_dump()

    user = await Users.find_one(Users.email == request_data.get("email"))

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Email or Password"
        )

    if password_helper.verify_password(
        request_data.get("password"),
        user.password
    ):
        token = make_token(str(user.id))
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Email or Password"
        )
