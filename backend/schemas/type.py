from pydantic import BaseModel
from typing import List, Optional


class TypeSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class TypeCreateSchema(BaseModel):
    name: str


class TypeUpdateSchema(TypeSchema):
    pass


class ListTypeSchema(BaseModel):
    types: List[Optional[TypeSchema]]
