from fastapi import FastAPI

from settings import description

from routers.me_router import me_router
from routers.user_router import user_router
from routers.accounts_router import account_router
from routers.user_manager import user_manage_router
from routers.transfer_router import transfer_router

app = FastAPI(
    title="Smart Wallet",
    description=description,
    docs_url="/"
)

app.include_router(user_router)
app.include_router(account_router)
app.include_router(user_manage_router)
app.include_router(me_router)
app.include_router(transfer_router)
