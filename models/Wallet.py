from enum import Enum
from typing import Dict, Optional

from pydantic import BaseModel

from models import User


class Currency(str, Enum):
    USD = "USD"
    EUR = "EUR"
    GBP = "GBP"
    BTC = "BTC"
    ETH = "ETH"
    SOL = "SOL"


class Wallet(BaseModel):
    wallet_id: int
    user: User
    balances: Dict[Currency, float] = {}


class WalletTransaction(BaseModel):
    wallet_transaction_id: int
    wallet_id: int
    source_currency: Currency
    target_currency: Currency
    source_amount: float
    exchange_rate: Optional[float] = None
