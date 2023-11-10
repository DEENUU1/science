from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from src.api import api_router
from src.database import Base, engine

app = FastAPI(title="Science")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(api_router)
Base.metadata.create_all(bind=engine)
