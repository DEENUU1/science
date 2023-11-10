from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, Text, Integer
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Type(Base):
    __tablename__ = "type"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)


class Author(Base):
    __tablename__ = "author"
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)


class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    short_desc = Column(Text, nullable=True)
    url = Column(String, nullable=False)
    is_free = Column(Boolean, default=False)
    published_date = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now(), default=None)
    type_id = Column(Integer, ForeignKey('type.id'), nullable=True)
    type = relationship('Type', back_populates='data', nullable=True)
    authors = relationship('Author', secondary='data_author', back_populates='data', nullable=True)
