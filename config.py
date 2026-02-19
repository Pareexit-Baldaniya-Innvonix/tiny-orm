import os
from dotenv import load_dotenv

# load .env file into environment variables
load_dotenv()


# collecting connection data from os
class Settings:
    db_host: str = os.getenv("DB_HOST")
    db_user: str = os.getenv("DB_USER")
    db_password: str = os.getenv("DB_PASSWORD")
    db_name: str = os.getenv("DB_NAME")


db_settings = Settings()
