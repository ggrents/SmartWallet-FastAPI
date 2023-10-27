from starlette.responses import JSONResponse

from models import User, Account
from sqlalchemy.orm import Session
from schemas import GetUserSchema, CreateUpdateUserSchema, AccountSchema


def get_accounts_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(Account).filter(user_id=user_id).offset(skip).limit(limit).all()


def get_account_by_id(db: Session, id: int):
    return db.query(Account).filter(Account.id == id).first()


def remove_account(db: Session, id: int):
    _acc = get_account_by_id(db, id)
    db.query(Account).delete(_acc)
    db.commit()
    return JSONResponse(content={"detail": "OK"}, status_code=200)


def create_account(db: Session, account: AccountSchema):
    _account = Account(
        user_id=account.user_id,
        default_currency_id=account.default_currency_id,
        balance=account.balance
    )

    db.add(_account)
    db.commit()
    db.refresh(_account)
    return _account


def update_account(db: Session, acc_id: int, account: AccountSchema):
    _account = get_account_by_id(db=db, id=acc_id)

    _account.user_id = account.user_id
    _account.default_currency_id = account.default_currency_id
    _account.balance = account.balance

    db.commit()
    db.refresh(_account)
    return _account
