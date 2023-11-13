from typing import Any, Optional, Annotated
from fastapi import APIRouter, Depends, Request, Query
from sqlalchemy.orm import Session
from ..repository.data import data
from ..database import get_db
from ..schemas.data import ListDataSchema, DataResponseSchema

router = APIRouter()


@router.get("/", response_model=ListDataSchema)
async def get_all(db: Session = Depends(get_db), f: Annotated[bool | None, Query()] = None) -> Any:
    if f:
        data_list = data.get_frees(db)
    else:
        data_list = data.get_list(db)

    return {"count": len(data_list), "data": data_list}


@router.post("/search", response_model=ListDataSchema)
async def search(db: Session = Depends(get_db), query: Annotated[str, Query(min_length=1)] = None) -> Any:
    data_list = data.search(db, query)
    return {"count": len(data_list), "data": data_list}


@router.get("/{id}", response_model=DataResponseSchema)
async def get_data(id: int, db: Session = Depends(get_db)) -> Any:
    data_object = data.get(db, id)
    return {"data": data_object}
