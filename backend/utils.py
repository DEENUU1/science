from passlib.context import CryptContext

password_content = CryptContext(schemas=["bcrypt"], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_content.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_content.verify(plain_password, hashed_password)
