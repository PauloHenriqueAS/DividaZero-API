"""
term_controller.py

This module contains term-related routes.
"""

from fastapi import APIRouter
from app.services import term_service
from app.models import TermoDivida, Parcelamento

router = APIRouter()

@router.get("/GetTermById")
def get_term_by_id(id_termo:int):
    """
    Get term by id
    """
    return term_service.get_term_by_id(id_termo)

@router.get("/GetAllTermById")
def get_all_term_by_id(id_user: str):
    """
    Get data term by id
    """
    return term_service.get_all_term_by_id(id_user)

@router.post("/PostTerm")
def post_term(termo:TermoDivida, parcelas:Parcelamento):
    """
    Post Term
    """
    return term_service.post_term(termo,parcelas)

@router.patch("/UpdateTerm")
def update_term():
    """
    Update term
    """
    return term_service.update_term()


@router.get("/GetDados")
def get_dados():
    """
    Update term
    """
    return term_service.get_dados()