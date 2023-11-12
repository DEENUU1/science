from typing import Any
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from ..repository.data import data
from ..database import get_db
from starlette.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


@router.get("/")
async def get_all_schemas(request: Request, db: Session = Depends(get_db)) -> Any:
    data_list = data.get_list(db)
    return templates.TemplateResponse(
        "data.html",
        {
            "request": request,
            "data_list": data_list
        }
    )