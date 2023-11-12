from typing import Any
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from ..repository.data import data
from ..database import get_db
from starlette.templating import Jinja2Templates
from ..scrapers.nature import get_article_details


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


@router.get("/content/{id}")
async def get_data_content(id: int, db: Session = Depends(get_db)) -> Any:
    data_obj = data.get(db, id)
    content = None
    if data_obj.content is not None:
        content = data_obj.content
    elif data_obj.content is None and data_obj.is_free == True:
        content = get_article_details(db, data_obj.url)

    return content
