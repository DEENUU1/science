from sqlalchemy import TIMESTAMP, Column, String, Boolean, Text, Integer, Table, DateTime
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from .database import Base
from sqlalchemy.orm import relationship
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(255), unique=True, index=True)
    password = Column(String(100))
    is_active = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)
    verified_at = Column(DateTime, nullable=True, default=None)
    registered_at = Column(DateTime, nullable=True, default=None)
    updated_at = Column(DateTime, nullable=True, default=None, onupdate=datetime.now)
    created_at = Column(DateTime, nullable=False, server_default=func.now())


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
