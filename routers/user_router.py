from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.models import User
from database import get_db

user_router = APIRouter()


@user_router.get("/users/")
async def read_users(db: Session = Depends(get_db)):
    users = db.query(User).first()
    return users
