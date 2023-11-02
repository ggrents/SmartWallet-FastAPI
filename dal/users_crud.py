from fastapi import HTTPException
from starlette.responses import JSONResponse

from models import User
from sqlalchemy.orm import Session
from schemas import GetUserSchema, CreateUpdateUserSchema


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: CreateUpdateUserSchema):
    _user = User(
        username=user.username,
        email=user.email,
        hashed_password=user.password,
        balance=0

    )

    db.add(_user)
    db.commit()
    db.refresh(_user)
    return _user


def get_active_users(db: Session):
    return db.query(User).filter(User.is_active == "1").all()


def remove_user(db: Session, user_id: int):
    _user = get_user_by_id(db=db, user_id=user_id)
    if not _user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(_user)
    db.commit()
    return JSONResponse(content={"detail": "OK"}, status_code=200)


def update_user(db: Session, user_id: int, user: CreateUpdateUserSchema):
    _user = get_user_by_id(db=db, user_id=user_id)
    if not _user:
        raise HTTPException(status_code=404, detail="User not found")

    _user.username = user.username
    _user.email = user.email
    _user.hashed_password = user.password

    db.commit()
    db.refresh(_user)
    return _user
