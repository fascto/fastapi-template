from fastapi import FastAPI
from src.routers.v1.endpoints import health

app = FastAPI(title="{{ cookiecutter.project_name }}")

app.include_router(health.router, prefix="/api/v1")