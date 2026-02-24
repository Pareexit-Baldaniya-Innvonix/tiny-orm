from pydantic_settings import BaseSettings, SettingsConfigDict


# collecting connection data from environment variables
class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    db_host: str
    db_user: str
    db_password: str = ""
    db_name: str


# instantiate settings at module load time.
db_settings = Settings()
