import os
from dotenv import load_dotenv


load_dotenv()


class Settings:
    # JWT
    JWT_SECRET: str = os.getenv('SECRET_KEY')
    JWT_ALGORITHM: str = os.getenv('JWT_ALGORITHM', "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv('JWT_TOKEN_EXPIRE_MINUTES', 60)


def get_settings() -> Settings:
    return Settings()
