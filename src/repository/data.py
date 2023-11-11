from ..schemas.data import CreateDataSchema, UpdateDataSchema
from ..models import Data
from ..repository.base import RepositoryBase
from sqlalchemy.orm import Session


class RepositoryData(RepositoryBase[Data, CreateDataSchema, UpdateDataSchema]):

    def exists(self, db: Session, url: str) -> bool:
        return db.query(Data).filter(Data.url == url).first() is not None


data = RepositoryData(Data)
