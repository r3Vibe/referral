"""
v1 routes file
all the v1 routes like auth
profile... will be included here
"""

from fastapi import APIRouter
from app.routers.V1.auth import auth_router
from app.routers.V1.user import user_router

""" initialize the router """
router = APIRouter()

""" include auth routes """
router.include_router(auth_router.router)
router.include_router(user_router.router)
