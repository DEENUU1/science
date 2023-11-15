from fastapi import Header
from fastapi.security import OAuth2PasswordRequestForm
from ..repository.auth import get_token, get_refresh_token
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas.user import CreateUserRequest
from ..repository.user import create_user_account
from ..security import get_current_user

router = APIRouter()


@router.post("/token")
async def authenticate_user(data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return await get_token(data=data, db=db)


@router.post("/refresh")
async def refresh_access_token(refresh_token: str = Header(), db: Session = Depends(get_db)):
    return await get_refresh_token(token=refresh_token, db=db)


@router.post("/")
async def create_user(data: CreateUserRequest, db: Session = Depends(get_db)):
    await create_user_account(data=data, db=db)
    payload = {"message": "User account has been succesfully created."}
    return JSONResponse(content=payload)


@router.get("/user")
async def get_user(token: str = Header(), db: Session = Depends(get_db)):
    return get_current_user(token, db)
