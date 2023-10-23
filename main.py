from fastapi import FastAPI, Response
from starlette.responses import RedirectResponse, PlainTextResponse
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    id: int


app = FastAPI(
    title="Smart Wallet"
)


@app.get("/api/v1/{id}")
def main(response: Response, id: int, limit: str = "privet"):
    response.set_cookie(key="huy", value="pizda")

    return "hello!" + str(id) + limit + str(response.status_code)


@app.get("/old", response_class=RedirectResponse, status_code=302)
def old():
    return "https://metanit.com/python/fastapi"


@app.get("/new")
def new():
    return PlainTextResponse("Новая страница")


@app.post("/post")
def post(item: Item):
    return item.name
