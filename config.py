from functools import lru_cache
from pydantic import BaseModel, ConfigDict, ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict

# uncomment to see psycopg.pool logs
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logging.getLogger("psycopg.pool").setLevel(logging.INFO)

class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str
    
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

@lru_cache()
def get_settings():
    return Settings()
    

class Model(BaseModel):
    x: str
    model_config = SettingsConfigDict(extra='ignore')