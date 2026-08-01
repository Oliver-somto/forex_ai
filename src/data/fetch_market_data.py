import httpx
from src.config.settings import settings

TWELVE_DATA_URL = 'https://api.twelvedata.com/time_series'

async def get_forex_candles(symbol: str, interval: str = '1min', outputsize: int = 30) -> list[dict]:
    params = {
        'symbol': symbol,
        'interval': interval,
        'outputsize': outputsize,
        'apikey': settings.market_data_api_key
    }
    
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(TWELVE_DATA_URL, params = params)
        response.raise_for_status()
        data = response.json()
    
    if data.get('status') == 'error':
        raise ValueError(f'Twelve Data error: {data.get('message')}')
    
    return data['values']