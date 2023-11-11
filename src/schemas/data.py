from pydantic import BaseModel
from typing import List, Optional
from type import TypeSchema
from author import AuthorSchema


class DataSchema(BaseModel):
    id: int
    title: str
    short_desc: Optional[str]
    url: str
    is_free: bool = False
    published_date: Optional[str]
    type: Optional[TypeSchema]
    authors: Optional[List[AuthorSchema]]

    class Config:
        orm_mode = True


class ListDataSchema(BaseModel):
    data: List[Optional[DataSchema]]


class CreateDataSchema(DataSchema):
    pass


class UpdateDataSchema(DataSchema):
    pass
