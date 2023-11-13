from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from src.api import api_router
from src.database import Base, engine, get_db
from sqladmin import Admin
from src.admin import TypeAdmin, AuthorAdmin, DataAdmin
from src.scrapers.nature import run_nature_scraper
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Science")

app.mount("/src/static", StaticFiles(directory="src/static"), name="static")

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY"),
)
app.include_router(api_router)
Base.metadata.create_all(bind=engine)

admin = Admin(app, engine)
admin.add_view(TypeAdmin)
admin.add_view(AuthorAdmin)
admin.add_view(DataAdmin)
# run_nature_scraper(next(get_db()))
