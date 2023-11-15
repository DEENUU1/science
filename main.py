from fastapi import FastAPI, BackgroundTasks
from backend.api import api_router
from backend.database import Base, engine, get_db
from sqladmin import Admin
from backend.admin import TypeAdmin, AuthorAdmin, DataAdmin, UserAdmin
from backend.scrapers.nature import run_nature_scraper
from backend.scrapers.ng import run_ng
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.authentication import AuthenticationMiddleware
from backend.security import JWTAuth

app = FastAPI(title="Science")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://localhost:4200", "http://localhost:3000", "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(AuthenticationMiddleware, backend=JWTAuth())

app.include_router(api_router)
Base.metadata.create_all(bind=engine)

admin = Admin(app, engine)
admin.add_view(TypeAdmin)
admin.add_view(AuthorAdmin)
admin.add_view(DataAdmin)
admin.add_view(UserAdmin)

# @app.on_event("startup")
# async def run_nature_scraper_task():
#     BackgroundTasks().add_task(run_nature_scraper(next(get_db())))
#     print("Scraped all articles from nature")
#
#
# @app.on_event("startup")
# async def run_ng_scraper_task():
#     BackgroundTasks().add_task(run_ng(next(get_db())))
#     print("Scraped all articles from national geographic")
#
