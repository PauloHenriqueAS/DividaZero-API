
"""
app/services/image_service.py

This module contains dashboard-methods.
"""

from app.models import User
from app.repositorys.dashboard_repository import dashboard_repository

class DashboardService:
    """
    return algo
    """
    def get_dash_images(self):
        """
        return algo
        """
        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}

    def get_dash_users(self):
        """
        return algo
        """
        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}

    def get_dash_precessing_methods(self):
        """
        return algo
        """
        return {"mensagem": "dados para dash estatisticas dos metodos de processamento de imagem"}

dashboard_service = DashboardService()
