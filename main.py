"""
main.py

Configurations of FastAPI
"""

from fastapi import FastAPI
from app import (
    address_router,
    dashboard_router,
    debt_router,
    debtor_router,
    health_router,
    lender_router,
    parcels_router,
    term_router,
    user_router,
)

app = FastAPI(
    title="DividaZero-API",
    description="DívidaZero API - Regularização e Confissão de Dívidas",
    version="1.0.0",
    )

# app.include_router(authentication_router, prefix="/authentication", tags=["Authentication"])
app.include_router(address_router, prefix="/address", tags=["Address"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(debt_router, prefix="/debt", tags=["Debt"])
app.include_router(debtor_router, prefix="/debtor", tags=["Debtor"])
app.include_router(health_router, tags=["HealthCheck"])
app.include_router(lender_router, prefix="/lender", tags=["Lender"])
app.include_router(parcels_router, prefix="/parcels", tags=["Parcels"])
app.include_router(term_router, prefix="/term", tags=["Term"])
app.include_router(user_router, prefix="/user", tags=["User"])
