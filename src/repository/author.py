from ..schemas.author import AuthorCreateSchema, AuthorUpdateSchema
from ..models import Author
from ..repository.base import RepositoryBase
from sqlalchemy.orm import Session


class RepositoryAuthor(RepositoryBase[Author, AuthorCreateSchema, AuthorUpdateSchema]):

    def exists(self, db: Session, full_name: str) -> bool:
        return db.query(Author).filter(Author.full_name == full_name).first() is not None

    def get_by_full_name(self, db: Session, full_name: str) -> Author:
        return db.query(Author).filter(Author.full_name == full_name).first()


author = RepositoryAuthor(Author)
