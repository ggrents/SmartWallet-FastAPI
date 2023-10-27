from pydantic import BaseModel


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


class GetAccountSchema(BaseModel) :
    pass

class AccountSchema(BaseModel):
    user_id: int
    default_currency_id: int
    balance: float
