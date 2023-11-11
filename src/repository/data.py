from ..schemas.data import CreateDataSchema, UpdateDataSchema
from ..models import Data
from ..repository.base import RepositoryBase


class RepositoryData(RepositoryBase[Data, CreateDataSchema, UpdateDataSchema]):
    pass


data = RepositoryData(Data)
