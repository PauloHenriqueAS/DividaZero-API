"""
app/repository s/__init__.py

Imports a module from the package so that it is available when importing the package
"""
from .user_repository import user_repository 
from .dashboard_repository  import dashboard_repository 

__all__ = [
    "user_repository ",
    "dashboard_repository ",
]
