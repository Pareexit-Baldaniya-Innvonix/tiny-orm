import os
from pydantic import Field
from pydantic_settings import BaseSettings


# collecting connection data from environment variables
class Settings(BaseSettings):
    db_host: str = os.environ.get("DB_HOST", "")
    db_user: str = os.environ.get("DB_USER", "")
    db_password: str = os.environ.get("DB_PASSWORD", "")
    db_name: str = os.environ.get("DB_NAME", "")


# instantiate settings at module load time.
db_settings = Settings()
