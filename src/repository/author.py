from ..schemas.author import AuthorCreateSchema, AuthorUpdateSchema
from ..models import Author
from ..repository.base import RepositoryBase


class RepositoryAuthor(RepositoryBase[Author, AuthorCreateSchema, AuthorUpdateSchema]):
    pass


author = RepositoryAuthor(Author)
