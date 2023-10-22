from pydantic import BaseModel
from models import Wallet

class User(BaseModel):
    id: int
    username: str
    email: str
    wallet : Wallet



