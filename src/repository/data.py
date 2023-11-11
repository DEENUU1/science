from ..schemas.data import CreateDataSchema, UpdateDataSchema
from ..models import Data, Type, Author
from ..repository.base import RepositoryBase
from sqlalchemy.orm import Session
from typing import List


class RepositoryData(RepositoryBase[Data, CreateDataSchema, UpdateDataSchema]):

    def exists(self, db: Session, url: str) -> bool:
        return db.query(Data).filter(Data.url == url).first() is not None

    def create_by_fields(self, db: Session, title: str, url: str, short_desc: str, is_free: bool, published_date: str,
                         type: Type, authors: List[Author]) -> Data:
        data = Data(title=title, url=url, short_desc=short_desc, is_free=is_free, published_date=published_date,
                    type=type, authors=authors)
        db.add(data)
        db.commit()
        return data


data = RepositoryData(Data)
