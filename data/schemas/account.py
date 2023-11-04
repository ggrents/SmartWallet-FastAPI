from pydantic import BaseModel, Field
from data.schemas.currency import GetCurrencyScheme


class AccountScheme(BaseModel):
    user_id: int
    default_currency_id: int
    balance: float


class GetAccountScheme(BaseModel):
    currency: GetCurrencyScheme
    balance: float


class ReplData(BaseModel):
    amount: float = Field(..., gt=0)


class ReplAcc(BaseModel):
    amount: float = Field(..., gt=0)
    account_id: int


class CreateSelfAccount(BaseModel):
    default_currency_id: int


class UpdateAccountScheme(BaseModel):
    default_currency_id: int
    balance: float
