from sqlalchemy.orm import Session
from ..models import User
from ..schemas.user import CreateUserSchema


def create_user(session: Session, user: CreateUserSchema):
    new_user = User(**user.dict())
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def get_user(session: Session, email: str):
    return session.query(User).filter(User.email == email).first()
