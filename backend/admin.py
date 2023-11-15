from sqladmin import ModelView
from .models import Type, Data, Author, User


class TypeAdmin(ModelView, model=Type):
    column_list = [Type.id, Type.name]
    column_searchable_list = [Type.name]
    name_plural = "Types"
    page_size = 50
    page_size_options = [25, 50, 100, 200]


class DataAdmin(ModelView, model=Data):
    column_list = [Data.id, Data.title, Data.type, Data.authors, Data.is_free, Data.published_date]
    column_searchable_list = [Data.title, Data.type, Data.authors, Data.is_free]
    name_plural = "Datas"
    page_size = 50
    page_size_options = [25, 50, 100, 200]


class AuthorAdmin(ModelView, model=Author):
    column_list = [Author.id, Author.full_name]
    column_searchable_list = [Author.full_name]
    name_plural = "Authors"
    page_size = 50
    page_size_options = [25, 50, 100, 200]


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.is_active]
    column_searchable_list = [User.email]
    name_plural = "Users"
    page_size = 50
    page_size_options = [25, 50, 100, 200]
