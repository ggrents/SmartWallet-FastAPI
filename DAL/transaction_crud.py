from fastapi import HTTPException
from sqlalchemy import select, delete, insert, update
from starlette.responses import JSONResponse
from sqlalchemy.orm import Session
from data.models.account import Account
from data.models.transaction import Transaction
from data.schemas.account import AccountScheme, UpdateAccountScheme
from data.schemas.transaction import MakeTransactionScheme, GetTransactionScheme


def get_transactions(db: Session):
    query = select(Transaction)
    result = db.execute(query).scalars().all()
    if not result:
        return []
    return result


def create_transaction(db: Session, transaction: MakeTransactionScheme):
    query = insert(Transaction).values(sender_account_id=transaction.sender_account_id,
                                       receiver_account_id=transaction.receiver_account_id,
                                       amount=transaction.amount)

    db.execute(query)
    db.commit()

    return transaction


def get_transaction_by_id(db: Session, id: int):
    query = select(Transaction).filter(Transaction.id == id)
    result = db.execute(query).scalar()
    if not result:
        raise HTTPException(status_code=404, detail="Transaction is not exist")
    return result


def delete_transaction(db: Session, id: int):
    _tr = get_transaction_by_id(db, id)
    if not _tr:
        raise HTTPException(status_code=404, detail="Transaction is not exist")

    query = delete(Transaction).where(Transaction.id == id)
    db.execute(query)
    db.commit()

    return JSONResponse(content={"detail": "OK"}, status_code=200)
