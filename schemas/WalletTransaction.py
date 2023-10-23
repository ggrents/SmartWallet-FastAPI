from typing import Optional

from pydantic import BaseModel

from schemas.Wallet import Currency


class WalletTransaction(BaseModel):
    wallet_transaction_id: int
    wallet_id: int
    source_currency: Currency
    target_currency: Currency
    source_amount: float
    exchange_rate: Optional[float] = None
