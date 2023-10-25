from urllib.request import Request
from sqlalchemy import MetaData
from fastapi import FastAPI, Response, Cookie
from starlette.responses import RedirectResponse, PlainTextResponse, JSONResponse, HTMLResponse
from pydantic import BaseModel
from starlette.templating import Jinja2Templates
from database import engine

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Wallet"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Item(BaseModel):
    name: str
    id: int


templates = Jinja2Templates(directory="templates")


# @app.get("/", response_class=HTMLResponse)
# def read_root(request: Request):
#    return templates.TemplateResponse("index.html", {"request": request, "title": "FastAPI Template", "content": "Hello, this is FastAPI!"})

@app.get("/api/v1/{id}", tags=["dicks"])
def main(response: Response, id: int, limit: str = "privet"):
    response.set_cookie(key="huy", value="pizda")

    return "hello!" + str(id) + limit + str(response.status_code)


@app.get("/old", response_class=RedirectResponse, status_code=302, tags=["dicks", "eee"])
def old():
    return "https://metanit.com/python/fastapi"


@app.post("/pos", status_code=200)
def p(item: Item, response: Response, c=Cookie()):
    response.headers["dakl"] = "dad"
    return {"cookie": "c"}


@app.get("/new")
def new():
    return Item(name="artem", id=5)


@app.post("/post")
def post(item: Item):
    return item.name
