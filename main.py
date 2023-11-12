from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware

from src.api import api_router
from src.database import Base, engine, get_db
from sqladmin import Admin
from src.admin import TypeAdmin, AuthorAdmin, DataAdmin
# from nature import run_nature_scraper
from fastapi.staticfiles import StaticFiles


app = FastAPI(title="Science")


app.mount("/src/static", StaticFiles(directory="src/static"), name="static")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)
Base.metadata.create_all(bind=engine)


admin = Admin(app, engine)
admin.add_view(TypeAdmin)
admin.add_view(AuthorAdmin)
admin.add_view(DataAdmin)
# run_nature_scraper(next(get_db()))
