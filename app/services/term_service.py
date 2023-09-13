
"""
app/services/term_service.py

This module contains term-methods.
"""

from app.models import User
from app.repositorys.term_repository import term_repository

class TermService:
    """
    Term Service
    """
    def get_term_by_id(self):
        """
        Get data term by id
        """
        return term_repository.get_term_by_id()

    def post_term(self):
        """
        Insert new data term
        """
        return term_repository.post_term()

    def update_term(self):
        """
        Update term data
        """
        return term_repository.update_term()

term_service = TermService()
