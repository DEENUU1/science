import os

from sqlalchemy import TIMESTAMP, Column, String, Boolean, Text, Integer, Table, UniqueConstraint, PrimaryKeyConstraint, LargeBinary
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from .database import Base
from sqlalchemy.orm import relationship
import bcrypt
import jwt
from dotenv import load_dotenv

load_dotenv()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(LargeBinary, nullable=False)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    UniqueConstraint("email", name="uq_user_email")
    PrimaryKeyConstraint("id", name="pk_user_id")

    @staticmethod
    def hash_password(password) -> bytes:
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def validate_password(self, password) -> bool:
        return bcrypt.checkpw(password.encode(), self.hashed_password)

    def generate_token(self) -> dict:
        return {
            "access_token": jwt.encode(
                {"full_name": self.full_name, "email": self.email},
                os.getenv("SECRET_KEY")
            )
        }


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    datas = relationship('Data', secondary='data_author', back_populates='authors')


class Type(Base):
    __tablename__ = "type"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    datas = relationship('Data', back_populates='type')


class Data(Base):
    __tablename__ = "datas"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    short_desc = Column(Text, nullable=True)
    content = Column(Text, nullable=True)
    url = Column(String, nullable=False)
    is_free = Column(Boolean, default=False)
    published_date = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now(), default=None)
    type_id = Column(Integer, ForeignKey('type.id'), nullable=True)
    type = relationship('Type', back_populates='datas')
    authors = relationship('Author', secondary='data_author', back_populates='datas')


data_author = Table("data_author", Base.metadata,
                    Column("data_id", Integer, ForeignKey("datas.id")),
                    Column("author_id", Integer, ForeignKey("authors.id"))
                    )
