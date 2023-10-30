from datetime import timedelta, datetime

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from sqlalchemy.orm import Session

import schemas
from dependencies import get_db

from models import User
from database import Base, SECRET_KEY


ACCESS_TOKEN_EXPIRE_MINUTES = 30


def get_token(authorization: str = Depends(OAuth2PasswordBearer(tokenUrl="/login"))):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        token = authorization.split("Bearer ")[1]
        return token
    except IndexError:
        raise credentials_exception
    except Exception:
        raise credentials_exception


def get_current_user(token: str = Depends(get_token), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        db_user = db.query(User).filter(User.id == int(user_id)).first()
        if db_user is None:
            raise credentials_exception
        return db_user
    except Exception:
        raise credentials_exception


