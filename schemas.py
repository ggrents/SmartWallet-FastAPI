from typing import Optional

from pydantic import BaseModel


class SignUpUser(BaseModel):
    username: str
    email: str
    password: str


class LoginUser(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class DataToken(BaseModel):
    id: Optional[str] = None


class CreateUpdateUserSchema(BaseModel):
    username: str
    email: str
    is_active: bool
    password: str


class AccountSchema(BaseModel):
    user_id: int
    default_currency_id: int
    balance: float


class GetCurrencySchema(BaseModel):
    currency_code: str
    currency_symbol: str
    exchange_rate : float


class GetAccountSchema(BaseModel):
    currency: GetCurrencySchema
    balance: float

class ReplData(BaseModel) :
    amount : float


class UpdateAccountSchema(BaseModel):
    default_currency_id: int
    balance: float


class GetUserSchema(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    balance: float
    accounts: list[GetAccountSchema]
