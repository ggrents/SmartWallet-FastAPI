from datetime import datetime

from pydantic import BaseModel


class GetTransactionScheme(BaseModel):
    id: int
    sender_account_id: int
    receiver_account_id: int
    transaction_date: datetime
    amount: float


class MakeTransactionScheme(BaseModel):
    sender_account_id: int
    receiver_account_id: int
    amount: float


