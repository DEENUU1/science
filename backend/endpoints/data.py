from typing import Any, Annotated
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from ..repository.data import data
from ..database import get_db
from ..schemas.data import ListDataSchema, DataResponseSchema

router = APIRouter()


@router.get("/", response_model=ListDataSchema)
async def get_all(db: Session = Depends(get_db), f: Annotated[bool | None, Query()] = None) -> Any:
    """
    Returns all articles from the database and allows to filter them by is_free field
    """
    if f:
        data_list = data.get_frees(db)
    else:
        data_list = data.get_list(db)

    return {"count": len(data_list), "data": data_list}


@router.post("/search", response_model=ListDataSchema)
async def search(db: Session = Depends(get_db), query: Annotated[str, Query(min_length=1)] = None) -> Any:
    """
    Search articles based on a given query
    """
    data_list = data.search(db, query)
    return {"count": len(data_list), "data": data_list}


@router.get("/{id}", response_model=DataResponseSchema)
async def get_data(id: int, db: Session = Depends(get_db)) -> Any:
    """
    Retrieve data by id from the database.
    """
    data_object = data.get(db, id)
    return {"data": data_object}
