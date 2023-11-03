from typing import Optional

from pydantic import BaseModel, Field

from data.schemas.account import GetAccountScheme


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


class CreateUpdateUserScheme(BaseModel):
    username: str
    email: str
    is_active: bool
    password: str


class GetUserScheme(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool
    balance: float
    accounts: list[GetAccountScheme]
