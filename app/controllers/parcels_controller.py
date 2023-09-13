"""
lender_controller.py

This module contains debt-related routes.
"""

from fastapi import APIRouter
from app.services import parcels_service

router = APIRouter()

@router.get("/GetParcelsById")
def get_parcels_by_id():
    """
    Get parcels by id
    """
    return parcels_service.get_parcels_by_id()

@router.get("/GetParcelsByTerm")
def get_parcels_by_term():
    """
    Get parcels by term
    """
    return parcels_service.get_parcels_by_term()

@router.post("/PostParcels")
def post_parcels():
    """
    Post parcels
    """
    return parcels_service.post_parcels()

@router.patch("/UpdateParcels")
def update_parcels():
    """
    Update parcels
    """
    return parcels_service.update_parcels()
