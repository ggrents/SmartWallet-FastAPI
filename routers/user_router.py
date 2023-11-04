from typing import Annotated
from fastapi import APIRouter, Depends, Path, Body, HTTPException
from sqlalchemy.orm import Session

from data.schemas.user import GetUserScheme, CreateUpdateUserScheme
from dependencies import get_db
from dal import users_crud as crud

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.get("/", response_model=list[GetUserScheme])
async def get_users(db: Session = Depends(get_db), skip: int = 0,
                    limit: int = 10):
    users = crud.get_users(db, skip=skip, limit=limit)

    if not users:
        raise HTTPException(status_code=404, detail="Users not found")

    return users


@user_router.get("/{user_id}", response_model=GetUserScheme)
async def get_user_by_id(user_id: Annotated[int, Path()], db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@user_router.get("/active/true")
async def get_active_users(db: Session = Depends(get_db)):
    users = crud.get_active_users(db)

    if not users:
        raise HTTPException(status_code=404, detail="Users not found")

    return users


@user_router.post("/", response_model=CreateUpdateUserScheme)
async def create_user(user: Annotated[CreateUpdateUserScheme, Body(example={
    "username": "Your Username!",
    "email": "Your Email",
    "is_active": True,
    "password": "Your password"
})], db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@user_router.delete("/{user_id}")
async def remove_user(user_id: Annotated[int, Path()], db: Session = Depends(get_db)):
    return crud.remove_user(db, user_id)
