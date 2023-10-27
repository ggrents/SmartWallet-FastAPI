from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from models import User
from database import get_db
from schemas import GetUserSchema, CreateUpdateUserSchema, AccountSchema
from DAL import users_crud, accounts_crud

account_router = APIRouter(prefix="/accounts")


@account_router.get("/user/{user_id}", response_model=list[AccountSchema])
async def get_accounts_by_user(user_id: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    accs = accounts_crud.get_accounts_by_user(db, user_id=user_id, skip=skip, limit=limit)
    return accs


@account_router.get("/{acc_id}", response_model=GetUserSchema)
async def get_account_by_id(acc_id: int = Path(), db: Session = Depends(get_db)):
    acc = accounts_crud.get_account_by_id(db, acc_id)
    return acc


@user_router.get("/active/true")
async def get_active_users(db: Session = Depends(get_db)):
    users = users_crud.get_active_users(db)
    return users


@user_router.post("/", response_model=GetUserSchema)
async def create_user(user: CreateUpdateUserSchema, db: Session = Depends(get_db)):
    return users_crud.create_user(db, user)


@user_router.put("/{user_id}", response_model=GetUserSchema)
async def update_user(user_id: int, user: CreateUpdateUserSchema, db: Session = Depends(get_db)):
    return users_crud.update_user(db, user_id, user)


@user_router.delete("/{user_id}")
async def remove_user(user_id: int, db: Session = Depends(get_db)):
    return users_crud.remove_user(db, user_id)
