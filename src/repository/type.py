from ..schemas.type import TypeCreateSchema, TypeUpdateSchema
from ..models import Type
from ..repository.base import RepositoryBase


class RepositoryType(RepositoryBase[Type, TypeCreateSchema, TypeUpdateSchema]):
    pass


types = RepositoryType(Type)
