from fastapi import APIRouter
from .endpoints import type

api_router = APIRouter()
api_router.include_router(type.router, prefix="/type", tags=["type"])
