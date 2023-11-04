from pydantic import BaseModel


class GetCurrencyScheme(BaseModel):
    currency_code: str
    currency_symbol: str
    exchange_rate: float
