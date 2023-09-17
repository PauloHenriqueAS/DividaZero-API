
"""
app/services/debt_service.py

This module contains debt-methods.
"""

from app.models import User
from app.repositorys.debt_repository import debt_repository

class DebtService:
    """
    Debt Service
    """
    def get_debt_by_id(self,id:int):
        """
        Get data address by id
        """
        return debt_repository.get_debt_by_id(id)

    def get_all_debt_by_user(self,id_devedor:str):
        """
        Get all data address by id devedor
        """
        return debt_repository.get_all_debt_by_user(id_devedor)
    
    def post_debt(self):
        """
        Insert new data debt
        """
        return debt_repository.post_debt()

    def update_debt(self):
        """
        Update debt data
        """
        return debt_repository.update_debt()

debt_service = DebtService()
