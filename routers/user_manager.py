from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from data.models.user import User
from data.schemas.user import GetUserScheme, SignUpUser, LoginUser, Token
from dependencies import get_db


user_manage_router = APIRouter(tags=["User Manager"])


@user_manage_router.post("/signup", response_model=GetUserScheme, status_code=status.HTTP_201_CREATED)
def signup(user: SignUpUser, db: Session = Depends(get_db)) -> GetUserScheme:
    _user = User(username=user.username, email=user.email)
    _user.hash_password(user.password)
    db.add(_user)
    db.commit()
    return _user


@user_manage_router.post("/login")
def login(user: LoginUser, db: Session = Depends(get_db)):
    _user = db.query(User).filter(User.username == user.username).first()
    if _user is None or not _user.verify_password(user.password):
        raise HTTPException(401, detail="Invalid credentials")
    token = _user.generate_token()
    return Token(access_token=token, token_type='bearer')
