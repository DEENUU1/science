from fastapi import FastAPI
from src.api import api_router
from src.database import Base, engine, get_db
from sqladmin import Admin
from src.admin import TypeAdmin, AuthorAdmin, DataAdmin
from src.scrapers.nature import run_nature_scraper
from src.scrapers.ng import run_ng
from dotenv import load_dotenv
import os
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI(title="Science")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:4200", "http://localhost:3000", "http://localhost:8080"],
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
# run_ng(next(get_db()))
