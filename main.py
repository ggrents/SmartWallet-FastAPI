from fastapi import FastAPI, Depends
from starlette.requests import Request

import models
from database import engine
from routers.user_router import user_router
from routers.accounts_router import account_router
from routers.user_manager import user_manage_router
from dependencies import get_current_user
from schemas import GetUserSchema

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Wallet"
)

app.include_router(user_router)
app.include_router(account_router)
app.include_router(user_manage_router)


@app.get("/me")
def profile(current_user: models.User = Depends(get_current_user)) -> GetUserSchema:

    return current_user

#@app.get()

