"""
app/repositorys/__init__.py

Imports a module from the package so that it is available when importing the package
"""

from .address_repository  import address_repository 
from .dashboard_repository  import dashboard_repository 
from .debt_repository  import debt_repository 
from .debtor_repository  import debtor_repository 
from .lender_repository  import lender_repository 
from .parcels_repository  import parcels_repository 
from .term_repository  import term_repository 
from .user_repository import user_repository 

__all__ = [
    "address_repository",
    "dashboard_repository",
    "debt_repository",
    "debtor_repository",
    "lender_repository",
    "parcels_repository",
    "term_repository",
    "user_repository",
]
