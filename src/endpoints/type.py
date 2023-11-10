from typing import Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..repository.type import types
from ..schemas.type import TypeSchema, TypeCreateSchema
from ..database import get_db

router = APIRouter()


@router.post("/", response_model=TypeSchema)
def create_type(*, db: Session = Depends(get_db), type_in: TypeCreateSchema) -> Any:
    item = types.create(db=db, obj_in=type_in)
    return item
