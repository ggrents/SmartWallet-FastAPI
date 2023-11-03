from typing import Annotated

from _decimal import Decimal
from fastapi import APIRouter, Depends, HTTPException, Body, Query
from sqlalchemy import select, update, insert
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import JSONResponse

from dal import accounts_crud
from dependencies import get_current_user, get_db
from models import User, Account, Currency
from schemas import GetUserSchema, GetAccountSchema, GetCurrencySchema, ReplData, CreateSelfAccount, AccountSchema, \
    ReplAcc

me_router = APIRouter(prefix="/me", tags=["Me"])
