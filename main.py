from fastapi import FastAPI

import models
from database import engine
from routers.user_router import user_router
from routers.accounts_router import account_router


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Wallet"
)

app.include_router(user_router)
app.include_router(account_router)

