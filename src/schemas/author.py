from pydantic import BaseModel
from typing import List, Optional


class AuthorSchema(BaseModel):
    id: int
    full_name: str

    class Config:
        orm_mode = True


class AuthorCreateSchema(BaseModel):
    full_name: str


class ListAuthorSchema(BaseModel):
    authors: List[Optional[AuthorSchema]]
