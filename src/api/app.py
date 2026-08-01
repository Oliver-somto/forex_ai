from fastapi import FastAPI, HTTPException
from src.data.fetch_market_data import get_forex_candles
from src.api.schemas import Candle

app = FastAPI(title='Project Oracle API', version='0.1.0')

@app.get('/')
def root():
    return {'status': 'ok', 'message': 'Project Oracle is alive'}

@app.get('/prices/{pair}', response_model= list[Candle])
async def get_prices(pair: str, interval: str = '1min', outputsize: int = 30):
    formatted_symbol = f'{pair[:3]}/{pair[3:]}'
    try:
        return await get_forex_candles(formatted_symbol, interval, outputsize)
    except ValueError as e:
        raise HTTPException(status_code= 502, detail= str(e))