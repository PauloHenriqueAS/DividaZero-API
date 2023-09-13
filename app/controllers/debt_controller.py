"""
debt_controller.py

This module contains debt-related routes.
"""

from fastapi import APIRouter
from app.services import debt_service

router = APIRouter()

@router.get("/GetDebtById")
def get_debt_by_id():
    """
    Get debt by id
    """
    return debt_service.get_debt_by_id()

@router.post("/PostDebt")
def post_debt():
    """
    Post Debt
    """
    return debt_service.post_debt()

@router.patch("/UpdateDebt")
def update_Debt():
    """
    Update debt
    """
    return debt_service.update_debt()
