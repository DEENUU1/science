import os
from dotenv import load_dotenv
from typing import List

load_dotenv()


class Settings:
    # JWT
    JWT_SECRET: str = os.getenv("JWT_SECRET")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("JWT_TOKEN_EXPIRE_MINUTES")

    # Fastapi
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    SQLITE_DATABASE_URL: str = os.getenv("SQLITE_DATABASE_URL")
    TITLE: str = os.getenv("PROJECT_NAME")
    CORS_ORIGINS: List[str] = os.getenv("BACKEND_CORS_ORIGINS")


def get_settings() -> Settings:
    return Settings()
