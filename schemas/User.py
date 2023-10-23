from pydantic import BaseModel
from schemas import Wallet


class User(BaseModel):
    id: int
    username: str
    email: str
    wallet : Wallet



