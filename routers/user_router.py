from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from models import User
from database import get_db
from schemas import GetUserSchema, CreateUpdateUserSchema
from DAL import users_crud as crud

user_router = APIRouter(prefix="/users")


@user_router.get("/", response_model=list[GetUserSchema])
async def get_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@user_router.get("/{user_id}", response_model=GetUserSchema)
async def get_user_by_id(user_id: int = Path(), db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    return user


@user_router.get("/active/true")
async def get_active_users(db: Session = Depends(get_db)):
    users = crud.get_active_users(db)
    return users


@user_router.post("/", response_model=GetUserSchema)
async def create_user(user: CreateUpdateUserSchema, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@user_router.put("/{user_id}", response_model=GetUserSchema)
async def update_user(user_id: int, user: CreateUpdateUserSchema, db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user)


@user_router.delete("/{user_id}")
async def remove_user(user_id: int, db: Session = Depends(get_db)):
    return crud.remove_user(db, user_id)
