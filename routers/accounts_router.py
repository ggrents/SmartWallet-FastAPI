from typing import Annotated

from fastapi import APIRouter, Depends, Path, Body, HTTPException

from sqlalchemy.orm import Session
from starlette import status

from data.schemas.account import AccountScheme, UpdateAccountScheme
from dependencies import get_db
from dal import accounts_crud

account_router = APIRouter(prefix="/accounts", tags=["Accounts"])


@account_router.get("/user/{user_id}", response_model=list[AccountScheme])
def get_accounts_by_user(user_id: Annotated[int, Path()], db: Session = Depends(get_db), skip: int = 0,
                               limit: int = 10):
    accs = accounts_crud.get_accounts_by_user(db, user_id=user_id, skip=skip, limit=limit)

    if not accs:
        raise HTTPException(status_code=404, detail="For this user accounts not found")

    return accs


@account_router.get("/{acc_id}", response_model=AccountScheme)
def get_account_by_id(acc_id: Annotated[int, Path()], db: Session = Depends(get_db)):
    acc = accounts_crud.get_account_by_id(db, acc_id)

    if not acc:
        raise HTTPException(status_code=404, detail="Account not found")

    return acc


@account_router.delete("/{acc_id}")
def remove_account(acc_id: Annotated[int, Path()], db: Session = Depends(get_db)):
    return accounts_crud.remove_account(db, acc_id)


@account_router.post("/", response_model=AccountScheme, status_code=status.HTTP_201_CREATED)
def create_account(account: AccountScheme = Body(example={
    "user_id": "ID of the user",
    "default_currency_id": "ID of the currency",
    "balance": 100
}), db: Session = Depends(get_db)):

    return accounts_crud.create_account(db, account)


@account_router.put("/{acc_id}", response_model=UpdateAccountScheme)
def update_account(acc_id: int, account: UpdateAccountScheme = Body(), db: Session = Depends(get_db)):
    return accounts_crud.update_account(db, acc_id, account)
