import os
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# path to the directory where files lives
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env_path = os.path.join(base_dir, ".env")  # finding .env file


# collecting connection data from os
class Settings(BaseSettings):
    db_host: str = Field(alias="DB_HOST")
    db_user: str = Field(alias="DB_USER")
    db_password: str = Field(alias="DB_PASSWORD", default="")
    db_name: str = Field(alias="DB_NAME")

    # check for .env file in rrot directory
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


db_settings = Settings()
