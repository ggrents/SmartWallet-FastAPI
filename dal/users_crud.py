from fastapi import HTTPException
from sqlalchemy import select, insert, delete, update
from starlette.responses import JSONResponse


from sqlalchemy.orm import Session

from data.models.user import User
from data.schemas.user import CreateUpdateUserScheme


def get_users(db: Session, skip: int = 0, limit: int = 100):
    query = select(User).offset(0).limit(limit)
    result = db.execute(query).scalars().all()

    return result


def get_user_by_id(db: Session, user_id: int):
    query = select(User).where(User.id == user_id)
    result = db.execute(query).scalar()

    return result


def create_user(db: Session, user: CreateUpdateUserScheme):
    query = insert(User).values(username=user.username,
                                email=user.email,
                                hashed_password=user.password,
                                balance=0)

    db.execute(query)

    db.commit()

    return JSONResponse(content={"detail": f"User {user.username} has registered"}, status_code=200)


def get_active_users(db: Session):
    query = select(User).where(User.is_active)
    result = db.execute(query).scalars().all()

    return result


def remove_user(db: Session, user_id: int):
    _user = get_user_by_id(db=db, user_id=user_id)
    if not _user:
        raise HTTPException(status_code=404, detail="User not found")

    query = delete(User).where(User.id == user_id)
    db.execute(query)

    db.commit()
    return JSONResponse(content={"detail": f"User {_user.username} has been deleted"}, status_code=200)


def update_user(db: Session, user_id: int, user: CreateUpdateUserScheme):
    _user = get_user_by_id(db=db, user_id=user_id)
    if not _user:
        raise HTTPException(status_code=404, detail="User not found")

    _user.username = user.username
    _user.email = user.email
    _user.hashed_password = user.password

    db.commit()
    db.refresh(_user)
    return _user
