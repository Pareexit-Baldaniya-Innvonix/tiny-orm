import os
from pydantic_settings import BaseSettings


# collecting connection data from environment variables
class Settings(BaseSettings):
    db_host: str = os.environ.get("DB_HOST", "localhost")
    db_user: str = os.environ.get("DB_USER", "root")
    db_password: str = os.environ.get("DB_PASSWORD", "")
    db_name: str = os.environ.get("DB_NAME", "school_db")


# instantiate settings at module load time.
db_settings = Settings()
