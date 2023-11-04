from datetime import datetime

from pydantic import BaseModel, Field

from data.schemas.account import GetAccountScheme


class GetTransactionScheme(BaseModel):
    id: int
    sender_account: GetAccountScheme
    receiver_account: GetAccountScheme
    transaction_date: datetime
    amount: float


class MakeTransactionScheme(BaseModel):
    sender_account_id: int = Field(..., gt=0)
    receiver_account_id: int = Field(..., gt=0)
    amount: float = Field(..., gt=0)

