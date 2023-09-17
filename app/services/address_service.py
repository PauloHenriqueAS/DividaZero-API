
"""
app/services/address_service.py

This module contains address-methods.
"""

from app.models import User
from app.repositorys.address_repository import address_repository

class AddressService:
    """
    Address Service
    """
    def get_address_by_cep(self):
        """
        Get data address by cep
        """
        return address_repository.get_address_by_cep()

    def get_address_by_id(self,id:int):
        """
        Get data address by id
        """
        return address_repository.get_address_by_id(id)

    def post_address(self):
        """
        Insert new data address
        """
        return address_repository.post_address()

    def update_address(self):
        """
        Update address data
        """
        return address_repository.update_address()

address_service = AddressService()
