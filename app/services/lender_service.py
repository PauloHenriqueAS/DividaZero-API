
"""
app/services/lender_service.py

This module contains lender-methods.
"""

from app.models import User
from app.repositorys.lender_repository import lender_repository

class LenderService:
    """
    Lender Service
    """
    def get_lerder_by_cpf(self):
        """
        Get data lender by cpf
        """
        return lender_repository.get_lerder_by_cpf()

    def post_lender(self):
        """
        Insert new data lender
        """
        return lender_repository.post_lender()

    def update_lender(self):
        """
        Update lender data
        """
        return lender_repository.update_lender()

lender_service = LenderService()
