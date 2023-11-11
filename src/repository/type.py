from ..schemas.type import TypeCreateSchema, TypeUpdateSchema
from ..models import Type
from ..repository.base import RepositoryBase
from sqlalchemy.orm import Session


class RepositoryType(RepositoryBase[Type, TypeCreateSchema, TypeUpdateSchema]):

    def exists(self, db: Session, name: str) -> bool:
        return db.query(Type).filter(Type.name == name).first() is not None

    def get_by_name(self, db: Session, name: str) -> Type:
        return db.query(Type).filter(Type.name == name).first()

    def create_by_fields(self, db: Session, name: str) -> Type:
        type = Type(name=name)
        db.add(type)
        db.commit()
        return type


types = RepositoryType(Type)
