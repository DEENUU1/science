from fastapi import APIRouter
import type_endpoint

api_router = APIRouter()
api_router.include_router(type_endpoint.router, prefix="/type", tags=["type"])