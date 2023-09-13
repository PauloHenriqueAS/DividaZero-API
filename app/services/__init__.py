"""
app/services/__init__.py

Imports a module from the package so that it is available when importing the package
"""
from .address_service import address_service
from .dashboard_service import dashboard_service
from .debt_service import debt_service
from .debtor_service import debtor_service
from .lender_service import lender_service
from .parcels_service import parcels_service
from .term_service import term_service
from .user_service import user_service

__all__ = [
    "address_service",
    "dashboard_service",
    "debt_service",
    "debtor_service",
    "lender_service",
    "parcels_service",
    "term_service",
    "user_service",
]
