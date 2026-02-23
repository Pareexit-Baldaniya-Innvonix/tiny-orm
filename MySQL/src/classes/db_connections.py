import mysql.connector
from settings import db_settings


# manage the connection settings using credentials loaded from settings
class DBConnection:

    @staticmethod
    def get_connection():
        try:
            connection = mysql.connector.connect(
                host=db_settings.db_host,
                user=db_settings.db_user,
                password=db_settings.db_password,
                database=db_settings.db_name,
            )
            return connection

        except Exception as error:
            print(f"Failed to connect to database: {error}")
