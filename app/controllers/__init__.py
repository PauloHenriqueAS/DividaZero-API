"""
app/controllers/__init__.py

Imports a module from the package so that it is available when importing the package
"""

#from .authentication_controller import router as authentication_router
from .address_controller import router as address_router
from .dashboard_controller import router as dashboard_router
from .debt_controller import router as debt_router
from .debtor_controller import router as debtor_router
from .health_controller import router as health_router
from .lender_controller import router as lender_router
from .parcels_controller import router as parcels_router
from .term_controller import router as term_router
from .user_controller import router as user_router
