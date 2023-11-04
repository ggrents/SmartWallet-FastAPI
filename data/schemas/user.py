from typing import Optional

from pydantic import BaseModel, Field, ValidationError, EmailStr
from pydantic.v1 import validator

from data.schemas.account import GetAccountScheme


class SignUpUser(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=8)

    @validator("password")
    def validate_password(cls, value):

        if not any(char.isdigit() for char in value):
            raise ValidationError("The password must contain at least one digit")

        if not any(char.isalpha() for char in value):
            raise ValidationError("The password must contain at least one letter")

        if not any(char.isalnum() or not char.isspace() for char in value):
            raise ValidationError("The password must contain at least one special character")

        return value


class LoginUser(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class DataToken(BaseModel):
    id: Optional[str] = None


class CreateUpdateUserScheme(BaseModel):
    username: str = Field(min_length=3, max_length=25)
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
