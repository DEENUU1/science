from ..schemas.data import CreateDataSchema, UpdateDataSchema
from ..models import Data, Type, Author
from ..repository.base import RepositoryBase
from sqlalchemy.orm import Session
from typing import List, Optional


class RepositoryData(RepositoryBase[Data, CreateDataSchema, UpdateDataSchema]):

    def exists(self, db: Session, url: str) -> bool:
        return db.query(Data).filter(Data.url == url).first() is not None

    def create_by_fields(self, db: Session, title: str, url: str, short_desc: str, is_free: bool, published_date: str,
                         type: Type, authors: List[Author], content: Optional[str] = None) -> Data:
        data = Data(title=title, url=url, short_desc=short_desc, is_free=is_free, published_date=published_date,
                    type=type, authors=authors, content=content)
        db.add(data)
        db.commit()
        return data

    def update_content(self, db: Session, data_id: int, content: str) -> Data:
        data = db.query(Data).filter(Data.id == data_id).first()
        data.content = content
        db.commit()
        return data

    def get_by_url(self, db: Session, url: str) -> Data:
        return db.query(Data).filter(Data.url == url).first()


data = RepositoryData(Data)
