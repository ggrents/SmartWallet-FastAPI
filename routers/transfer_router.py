from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from dal.transaction_crud import get_transactions, create_transaction, delete_transaction
from data.schemas.transaction import GetTransactionScheme, MakeTransactionScheme
from dependencies import get_db

transfer_router = APIRouter(prefix="/remmitances", tags=["Transfers"])


@transfer_router.get("", response_model=list[GetTransactionScheme])
async def get_remmitances(db: Session = Depends(get_db)):
    return get_transactions(db)


@transfer_router.post("")
async def make_remmitance(tranasction: MakeTransactionScheme, db: Session = Depends(get_db)):
    return create_transaction(db, tranasction)


@transfer_router.delete("/{tr_id}")
async def delete_remmitance(tr_id: int, db: Session = Depends(get_db)):
    return delete_transaction(db,tr_id)
