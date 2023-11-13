from pydantic import BaseModel
from typing import List, Optional
from .type import TypeSchema
from .author import AuthorSchema


class DataSchema(BaseModel):
    id: int
    title: str
    content: Optional[str] = None
    short_desc: Optional[str] = None
    url: str
    is_free: bool = False
    published_date: Optional[str] = None
    type: Optional[TypeSchema] = None
    authors: Optional[List[AuthorSchema]] = None

    class Config:
        orm_mode = True


class ListDataSchema(BaseModel):
    count: int = 0
    data: List[DataSchema]


class CreateDataSchema(DataSchema):
    pass


class UpdateDataSchema(DataSchema):
    pass


class DataResponseSchema(BaseModel):
    data: DataSchema
