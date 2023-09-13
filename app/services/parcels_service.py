
"""
app/services/parcels_service.py

This module contains parcels-methods.
"""

from app.models import User
from app.repositorys.parcels_repository import parcels_repository

class ParcelsService:
    """
    Parcels Service
    """
    def get_parcels_by_id(self):
        """
        Get parcels by id
        """
        return parcels_repository.get_parcels_by_id()

    def get_parcels_by_term(self):
        """
        Get parcels by id term
        """
        return parcels_repository.get_parcels_by_term()

    def post_parcels(self):
        """
        Insert new parcel data
        """
        return parcels_repository.post_parcels()
    
    def update_parcels(self):
        """
        Update new parcel data
        """
        return parcels_repository.update_parcels()

parcels_service = ParcelsService()
