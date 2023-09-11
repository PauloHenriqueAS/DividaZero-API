"""
app/services/__init__.py

Imports a module from the package so that it is available when importing the package
"""
from .user_service import user_service
from .dashboard_service import dashboard_service

__all__ = [
    "user_service",
    "dashboard_service",
]
