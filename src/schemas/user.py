from pydantic import BaseModel
from typing import Optional


class UserSchema(BaseModel):
    id: int
    emaiL: str
    first_name: str
    last_name: Optional[str]

    class Config:
        orm_mode = True


class UserCreateSchema(UserSchema):
    pass


class UserUpdateSchema(UserSchema):
    pass
