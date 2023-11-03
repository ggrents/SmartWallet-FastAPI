from data.models.user import User
from database import SessionLocal
from fastapi import Depends, HTTPException, status, Header

import jwt
from sqlalchemy.orm import Session

from database import Base
from settings import SECRET_KEY


def get_db():
    db = SessionLocal()
    try:
        yield db

    finally:
        db.close()


def get_token(authorization: str = Header(...)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could222 not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        return authorization.split("Bearer ")[1]

    except IndexError:
        raise credentials_exception
    except Exception:
        raise credentials_exception


def get_current_user(token: str = Depends(get_token), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could2222 not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        if not payload:
            raise credentials_exception
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        db_user = db.query(User).filter(User.id == int(user_id)).first()
        if db_user is None:
            raise credentials_exception
        return db_user
    except Exception:
        raise credentials_exception
