from .database import Base
from sqlalchemy import TIMESTAMP, Column, String, Boolean, Text
from sqlalchemy.sql import func
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Type(Base):
    __tablename__ = "type"
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    name = Column(String, nullable=False)


class Author(Base):
    __tablename__ = "author"
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    full_name = Column(String, nullable=False)


class Data(Base):
    __tablename__ = "data"
    id = Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    type_id = Column(GUID, ForeignKey('type.id'), nullable=False)
    type = relationship('Type', back_populates='data', nullable=True)
    title = Column(String, nullable=False)
    short_desc = Column(Text, nullable=True)
    authors = relationship('Author', secondary='data_author', back_populates='data', nullable=True)
    url = Column(String, nullable=False)
    is_free = Column(Boolean, nullable=False)
    published_date = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now(), default=None)
