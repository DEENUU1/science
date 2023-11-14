from fastapi import APIRouter
from .endpoints import data, auth

api_router = APIRouter()
api_router.include_router(data.router, prefix="", tags=["data"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
