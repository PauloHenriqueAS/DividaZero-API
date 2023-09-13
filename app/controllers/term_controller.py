"""
term_controller.py

This module contains term-related routes.
"""

from fastapi import APIRouter
from app.services import term_service

router = APIRouter()

@router.get("/GetTermById")
def get_term_by_id():
    """
    Get term by id
    """
    return term_service.get_term_by_id()

@router.post("/PostTerm")
def post_term():
    """
    Post Term
    """
    return term_service.post_term()

@router.patch("/UpdateTerm")
def update_term():
    """
    Update term
    """
    return term_service.update_term()
