from sqladmin import ModelView
from .models import Type, Data, Author


class TypeAdmin(ModelView, model=Type):
    column_list = [Type.id, Type.name]


class DataAdmin(ModelView, model=Data):
    column_list = [Data.id, Data.title, Data.type, Data.authors, Data.is_free, Data.published_date]


class AuthorAdmin(ModelView, model=Author):
    column_list = [Author.id, Author.full_name]
