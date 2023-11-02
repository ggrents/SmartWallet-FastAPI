from fastapi import HTTPException
from sqlalchemy import select, delete, insert, update
from starlette.responses import JSONResponse

from models import User, Account
from sqlalchemy.orm import Session
from schemas import GetUserSchema, CreateUpdateUserSchema, AccountSchema, GetAccountSchema, UpdateAccountSchema


def get_accounts_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    query = select(Account).where(Account.user_id == user_id)
    result = db.execute(query)
    _accs = result.scalars().all()
    return result


def get_account_by_id(db: Session, acc_id: int):
    query = select(Account).filter(Account.id == acc_id)
    result = db.execute(query).scalar()
    if not result:
        raise HTTPException(status_code=404, detail="Account is not exist")
    return result


def remove_account(db: Session, acc_id: int):
    _acc = get_account_by_id(db, acc_id)

    query = delete(Account).where(Account.id == acc_id)
    db.execute(query)
    db.commit()

    return JSONResponse(content={"detail": "OK"}, status_code=200)


def create_account(db: Session, account: AccountSchema):
    query = insert(Account).values(user_id=account.user_id,
                                   default_currency_id=account.default_currency_id,
                                   balance=account.balance)

    db.execute(query)

    db.commit()

    return account


def update_account(db: Session, acc_id: int, account: UpdateAccountSchema):
    _account = get_account_by_id(db=db, acc_id=acc_id)
    query = update(Account).values(user_id=_account.user_id if not account.user_id else account.user_id,
                                   default_currency_id=_account.default_currency_id if not account.default_currency_id else account.default_currency_id,
                                   balance=_account.balance if not account.balance else account.balance
                                   )

    db.execute(query)
    db.commit()
    db.refresh(_account)
    return _account
