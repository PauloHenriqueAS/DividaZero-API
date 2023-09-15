"""
user_controller.py

This module contains user-related routes.
"""

from fastapi import APIRouter
from app.models import User, UserWithEndereco
from app.services import user_service
router = APIRouter()

@router.post("/login")
def login(data_user: User):
    """
    Return status from user login
    """
    return user_service.login(data_user)

@router.get("/GetUsuarioByCode")
def get_user_by_code(email_user: str):
    """
    Return data from user by email
    """
    return user_service.get_user_by_code(email_user)

@router.post("/PostUser")
async def post_user(data: UserWithEndereco):
    """
    Post data from a new user
    # """
    return user_service.post_user(data)

@router.patch("/UpdatePasswordUser")
def update_password_user(data_user: User):
    """
    Update data user
    """
    return user_service.update_password_user(data_user)
