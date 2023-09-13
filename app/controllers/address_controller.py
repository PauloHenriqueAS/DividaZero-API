"""
address_controller.py

This module contains address-related routes.
"""

from fastapi import APIRouter
from app.services import address_service

router = APIRouter()

@router.get("/GetAddressByCep")
def get_address_by_cep():
    """
    Get address by cep
    """
    return address_service.get_address_by_cep()

@router.post("/PostAddress")
def post_address():
    """
    Post Address
    """
    return address_service.post_address()

@router.patch("/UpdateAddress")
def update_address():
    """
    Update Address
    """
    return address_service.update_address()
