from typing import Any, Annotated, Optional
from fastapi import APIRouter, Depends, Request, Query
from sqlalchemy.orm import Session
from ..repository.data import data
from ..database import get_db
from starlette.templating import Jinja2Templates


router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


@router.get("/")
async def get_all(request: Request, db: Session = Depends(get_db), f: Optional[bool] = False) -> Any:
    if f:
        data_list = data.get_frees(db)
    else:
        data_list = data.get_list(db)

    return templates.TemplateResponse(
        "data.html",
        {
            "request": request,
            "data_list": data_list
        }
    )


@router.get("/content/{id}")
async def get_data_content(id: int, db: Session = Depends(get_db)) -> Any:
    data_obj = data.get(db, id)
    return data_obj.content
