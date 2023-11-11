from fastapi import APIRouter
from .endpoints import type, data

api_router = APIRouter()
api_router.include_router(type.router, prefix="/type", tags=["type"])
api_router.include_router(data.router, prefix="", tags=["data"])
