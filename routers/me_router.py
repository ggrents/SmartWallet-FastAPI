from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dal import accounts_crud
from dependencies import get_current_user, get_db
from models import User, Account, Currency
from schemas import GetUserSchema, GetAccountSchema, GetCurrencySchema

me_router = APIRouter(prefix="/me", tags=["Me"])


@me_router.get("")
def profile(current_user: User = Depends(get_current_user)) -> GetUserSchema:
    return current_user


@me_router.get("/accounts")
async def get_my_accounts(current_user: User = Depends(get_current_user),
                          db: Session = Depends(get_db)) -> list[GetAccountSchema]:
    accs = accounts_crud.get_accounts_by_user(db, user_id=current_user.id, skip=0, limit=100)
    if not accs:
        raise HTTPException(status_code=404, detail="You do not have accounts!")

    return accs


@me_router.get("/currencies")
async def get_currencies(current_user: User = Depends(get_current_user),
                         db: Session = Depends(get_db)) -> list[GetCurrencySchema]:

    return db.query(Currency).all()
