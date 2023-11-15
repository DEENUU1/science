from pydantic import BaseModel
from typing import List, Optional


class AuthorSchema(BaseModel):
    id: Optional[int] = None
    full_name: Optional[str] = None

    class Config:
        orm_mode = True


class AuthorCreateSchema(BaseModel):
    full_name: str


class AuthorUpdateSchema(BaseModel):
    full_name: Optional[str]


class ListAuthorSchema(BaseModel):
    authors: List[Optional[AuthorSchema]]
