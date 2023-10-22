from fastapi import FastAPI

app = FastAPI(
    title="Smart Wallet"
)


@app.get("/huy/{id}")
def main(id: int, limit : str = "privet"):
    return "hello!" + str(id) + limit
