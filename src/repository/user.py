from ..schemas.user import UserCreateSchema, UserUpdateSchema
from ..models import User
from ..repository.base import RepositoryBase
from sqlalchemy.orm import Session


class RepositoryUser(RepositoryBase[User, UserCreateSchema, UserUpdateSchema]):

    def exists(self, db: Session, email: str) -> bool:
        return db.query(User).filter(User.email == email).first() is not None

    def get_by_email(self, db: Session, email: str) -> User:
        return db.query(User).filter(User.email == email).first()


user = RepositoryUser(User)
