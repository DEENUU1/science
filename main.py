from fastapi import FastAPI
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
# run_nature_scraper(next(get_db()))
# run_ng(next(get_db()))
