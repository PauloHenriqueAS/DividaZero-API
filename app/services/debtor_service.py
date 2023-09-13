
"""
app/services/debtor_service.py

This module contains debtor-methods.
"""

from app.models import User
from app.repositorys.debtor_repository import debtor_repository

class DebtorService:
    """
    Debtor Service
    """
    def get_debtor_by_cnpj(self):
        """
        Get data debtor by cnpj
        """
        return debtor_repository.get_debtor_by_cnpj()

    def post_debtor(self):
        """
        Insert new data debtor
        """
        return debtor_repository.post_debtor()

    def update_debtor(self):
        """
        Update debtor data
        """
        return debtor_repository.update_debtor()

debtor_service = DebtorService()
