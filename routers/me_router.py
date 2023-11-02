from typing import Annotated

from _decimal import Decimal
from fastapi import APIRouter, Depends, HTTPException, Body, Query
from sqlalchemy import select, update
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from dal import accounts_crud
from dependencies import get_current_user, get_db
from models import User, Account, Currency
from schemas import GetUserSchema, GetAccountSchema, GetCurrencySchema, ReplData

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


@me_router.get("/currencies", response_model=list[GetCurrencySchema])
async def get_currencies(
        db: Session = Depends(get_db)):
    query = select(Currency)
    result = db.execute(query).scalars().all()
    return result


@me_router.post("/replenishment")
async def replenish_balance(repl: Annotated[ReplData, Body()], user: User = Depends(get_current_user),
                            db: Session = Depends(get_db), ):
    try:
        query = update(User).where(User.id == user.id).values(balance=User.balance + Decimal(repl.amount))
        db.execute(query)
        db.commit()
        return JSONResponse(status_code=200, content={"detail" : "replenishment was successful"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@me_router.post("/accounts", response_model=GetAccountSchema)
async def create_account(acc : Annotated[Account, Body()], user: User = Depends(get_current_user),
                            db: Session = Depends(get_db), ) :
    pass