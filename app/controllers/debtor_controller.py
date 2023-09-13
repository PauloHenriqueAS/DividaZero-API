"""
debtor_controller.py

This module contains debtor-related routes.
"""

from fastapi import APIRouter
from app.services import debtor_service

router = APIRouter()

@router.get("/GetDebtorByCNPJ")
def get_debtor_by_cnpj():
    """
    Get debtor by id
    """
    return debtor_service.get_debtor_by_cnpj()

@router.post("/PostDebtor")
def post_debtor():
    """
    Post Debtor
    """
    return debtor_service.post_debtor()

@router.patch("/UpdateDebtor")
def update_Debt():
    """
    Update debtor
    """
    return debtor_service.update_debtor()
