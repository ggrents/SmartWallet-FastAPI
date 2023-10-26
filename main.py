from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from models import models
from database import engine, get_db
from models.models import User
from routers.user_router import user_router

#models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Wallet"
)

app.include_router(user_router)


@app.get("/ee")
def kk(db: Session = Depends(get_db)):
    return db.query(User).first()
