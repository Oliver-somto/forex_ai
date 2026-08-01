from pydantic import BaseModel

class Candle(BaseModel):
    datetime: str
    open: float
    high: float
    low: float
    close: float