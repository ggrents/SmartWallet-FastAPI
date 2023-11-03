from typing import Annotated

from fastapi import APIRouter, Depends, Path, Body, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from starlette.requests import Request
from starlette.responses import Response

from models import User
from dependencies import get_db
from schemas import GetUserSchema, CreateUpdateUserSchema, AccountSchema, GetAccountSchema, UpdateAccountSchema
from dal import users_crud, accounts_crud

account_router = APIRouter(prefix="/accounts", tags=["Accounts"])


@account_router.get("/user/{user_id}", response_model=list[AccountSchema])
async def get_accounts_by_user(user_id: Annotated[int, Path()], db: Session = Depends(get_db), skip: int = 0,
                               limit: int = 10):
    accs = accounts_crud.get_accounts_by_user(db, user_id=user_id, skip=skip, limit=limit)
    if not accs:
        raise HTTPException(status_code=404, detail="For this user accounts not found")
    return accs


@account_router.get("/{acc_id}", response_model=AccountSchema)
async def get_account_by_id(acc_id: Annotated[int, Path()], db: Session = Depends(get_db)):
    acc = accounts_crud.get_account_by_id(db, acc_id)
    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")
    return acc


@account_router.delete("/{acc_id}")
async def remove_account(acc_id: Annotated[int, Path()], db: Session = Depends(get_db)):
    return accounts_crud.remove_account(db, acc_id)


@account_router.post("/", response_model=AccountSchema, status_code=status.HTTP_201_CREATED)
async def create_account(account: AccountSchema = Body(example={
    "user_id": "ID of the user",
    "default_currency_id": "ID of the currency",
    "balance": 100
}), db: Session = Depends(get_db)):
    return accounts_crud.create_account(db, account)


@account_router.put("/{acc_id}", response_model=UpdateAccountSchema)
async def update_account(acc_id: int, account: UpdateAccountSchema = Body(), db: Session = Depends(get_db)):
    return accounts_crud.update_account(db, acc_id, account)
