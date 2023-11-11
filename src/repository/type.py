from ..schemas.type import TypeCreateSchema, TypeUpdateSchema
from ..models import Type
from ..repository.base import RepositoryBase
from sqlalchemy.orm import Session


class RepositoryType(RepositoryBase[Type, TypeCreateSchema, TypeUpdateSchema]):
    def __ini__(self):
        super().__init__(Type)

    def type_object_exists(self, db: Session, name: str) -> bool:
        return db.query(Type).filter(Type.name == name).first() is not None

    def get_by_name(self, db: Session, name: str) -> Type:
        return db.query(Type).filter(Type.name == name).first()


types = RepositoryType(Type)
