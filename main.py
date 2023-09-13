"""
main.py

Configurations of FastAPI
"""

from fastapi import FastAPI
from app import (
    user_router,
    health_router,
    dashboard_router,
)

def rodar_docker_compose():
    try:
        subprocess.run(['docker-compose', 'up'])
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

rodar_docker_compose()

app = FastAPI(
    title="DividaZero-API",
    description="DívidaZero API - Regularização e Confissão de Dívidas",
    version="1.0.0",
    )

#app.include_router(authentication_router, prefix="/authentication", tags=["Authentication"])
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(health_router, tags=["HealthCheck"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])
