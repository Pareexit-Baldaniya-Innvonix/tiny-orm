from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


# collecting connection data from environment variables or .env file
class Settings(BaseSettings):
    db_host: str = Field(alias="DB_HOST")
    db_user: str = Field(alias="DB_USER")
    db_password: str = Field(alias="DB_PASSWORD", default="")
    db_name: str = Field(alias="DB_NAME")

    # Read connection data from .env files
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


# instantiate settings at module load time.
db_settings = Settings()
