from fastapi import APIRouter
from .endpoints import data

api_router = APIRouter()
api_router.include_router(data.router, prefix="", tags=["data"])
