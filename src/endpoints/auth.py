from fastapi import APIRouter, Request, Depends
from starlette.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from authlib.integrations.starlette_client import OAuth, OAuthError
from dotenv import load_dotenv
import os
from ..repository.user import user as user_repo
from ..database import get_db
from sqlalchemy.orm import Session

load_dotenv()

oauth = OAuth()
oauth.register(
    name='google',
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    client_kwargs={
        'scope': 'email openid profile',
        'redirect_url': 'http://localhost:8000/auth/auth'
    }
)
router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


@router.get("/login")
async def login(request: Request):
    url = request.url_for('auth')
    return await oauth.google.authorize_redirect(request, url)


@router.get('/auth')
async def auth(request: Request, db: Session = Depends(get_db)):
    try:
        token = await oauth.google.authorize_access_token(request)
    except OAuthError as e:
        return templates.TemplateResponse(
            name='error.html',
            context={'request': request, 'error': e.error}
        )
    user = token.get('userinfo')
    if user:
        user_data = dict(user)
        request.session['user'] = user_data

        if not user_repo.exists(db, user_data["email"]):
            user_repo.create_by_fields(
                db,
                email=user_data["email"],
                first_name=user_data["given_name"],
                last_name=user_data.get("family_name", None),
            )

    return RedirectResponse('/')


@router.get('/logout')
def logout(request: Request):
    request.session.pop('user')
    return RedirectResponse('/')


@router.get("/current")
def get_current_user(request: Request):
    return request.session.get('user')
