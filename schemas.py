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


class GetUserSchema(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool


class CreateUpdateUserSchema(BaseModel):
    username: str
    email: str
    is_active: bool
    password: str


class GetAccountSchema(BaseModel):
    pass


class AccountSchema(BaseModel):
    user_id: int
    default_currency_id: int
    balance: float
