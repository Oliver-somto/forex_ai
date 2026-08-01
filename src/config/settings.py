from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    market_data_api_key: str = ''
    database_url: str = ''
    llm_api_key: str = ''
    
    class config:
        env_file = '.env'

settings = Settings()