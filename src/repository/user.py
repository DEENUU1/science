from ..schemas.user import UserCreateSchema, UserUpdateSchema
from ..models import User
from ..repository.base import RepositoryBase
from sqlalchemy.orm import Session
from typing import Optional


class RepositoryUser(RepositoryBase[User, UserCreateSchema, UserUpdateSchema]):

    def exists(self, db: Session, email: str) -> bool:
        return db.query(User).filter(User.email == email).first() is not None

    def get_by_email(self, db: Session, email: str) -> User:
        return db.query(User).filter(User.email == email).first()

    def create_by_fields(self, db: Session, email: str, first_name: str, last_name: Optional[str]):
        user = User(email=email, first_name=first_name, last_name=last_name)
        db.add(user)
        db.commit()
        return user


user = RepositoryUser(User)
