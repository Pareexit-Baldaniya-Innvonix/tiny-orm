import mysql.connector
from settings import db_settings


# manage the connection settings using config file/.env variables
class Config:
    @staticmethod
    def get_connection():
        return mysql.connector.connect(
            host=db_settings.db_host,
            user=db_settings.db_user,
            password=db_settings.db_password,
            database=db_settings.db_name,
        )
