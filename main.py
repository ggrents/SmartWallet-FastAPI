from fastapi import FastAPI, Depends
import models
from database import engine
from routers.me_router import me_router
from routers.user_router import user_router
from routers.accounts_router import account_router
from routers.user_manager import user_manage_router

from settings import description

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Wallet",
    description=description
)

app.include_router(user_router)
app.include_router(account_router)
app.include_router(user_manage_router)
app.include_router(me_router)

