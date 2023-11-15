from pydantic import BaseModel
from typing import List, Optional


class TypeSchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

    class Config:
        orm_mode = True


class TypeCreateSchema(BaseModel):
    name: str


class TypeUpdateSchema(TypeSchema):
    pass


class ListTypeSchema(BaseModel):
    types: List[Optional[TypeSchema]]
