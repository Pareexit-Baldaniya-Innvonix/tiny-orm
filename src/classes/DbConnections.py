import mysql.connector
from settings import db_settings


# manage the connection settings using credentials loaded from settings
class DBConnection:

    @staticmethod  # if not using then need to create instance 'db = DBConnection()' first then call 'db.get_connection()'
    def get_connection():  # utility function that create & return a connection using settings, not read or modify any class/instance state, that's why using staticmethod
        try:
            connection = mysql.connector.connect(
                host=db_settings.db_host,
                user=db_settings.db_user,
                password=db_settings.db_password,
                database=db_settings.db_name,
            )
            return connection

        except mysql.connector.Error as error:
            print(f"Failed to connect to database: {error}")
