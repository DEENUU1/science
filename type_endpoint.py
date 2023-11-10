from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import repository, models, schemas, database


router = APIRouter()



@router.post("/", response_model=schemas.TypeSchema)
def create_type(
        *,
        db: Session = Depends(database.get_db),
        type_in: schemas.TypeCreateSchema,
) -> Any:
    item = repository.types.create(db=db, obj_in=type_in)
    return item
