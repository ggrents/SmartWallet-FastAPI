from fastapi import FastAPI, Depends
from starlette.requests import Request

import models
from database import engine
from routers.user_router import user_router
from routers.accounts_router import account_router
from routers.user_manager import user_manage_router
from auth import get_current_user

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Wallet"
)

app.include_router(user_router)
app.include_router(account_router)
app.include_router(user_manage_router)


@app.get("/")
def m(request : Request, current_user: models.User = Depends(get_current_user)):
    request.headers["Authorization"] = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiZXhwIjoxNjk4NzM5ODA1LjE0OTIwNH0.22VmVohsDxh5kKyuiPuJsVFvokyTy-bGdDpaTFE8LXw"
    return f"{models.User.username} qqq!"
