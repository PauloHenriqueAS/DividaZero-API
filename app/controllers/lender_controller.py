"""
lender_controller.py

This module contains lender-related routes.
"""

from fastapi import APIRouter
from app.services import lender_service

router = APIRouter()

@router.get("/GetLenderByCPF")
def get_lerder_by_cpf():
    """
    Get lender by id
    """
    return lender_service.get_lerder_by_cpf()

@router.get("/GetLenderById")
def get_lerder_by_id(id:str):
    """
    Get lender by id
    """
    return lender_service.get_lerder_by_id(id)


@router.post("/PostLender")
def post_lender():
    """
    Post lender
    """
    return lender_service.post_lender()

@router.patch("/UpdateLender")
def update_lender():
    """
    Update lender
    """
    return lender_service.update_lender()
