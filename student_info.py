from pydantic import BaseModel
from config import db_settings
import mysql.connector
from typing import Optional


# Pydantic method to define the structure of Student object
class Student(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    dept: str


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


# global database object
conn = Config.get_connection()
cursor = conn.cursor()


# CRUD operations
class StudentInfo:

    # create students table
    @staticmethod
    def create_table():
        try:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS students(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                email VARCHAR(255),
                dept CHAR(50))
            """
            )
            print("\n--- Table created successfully. ---")
        except Exception as e:
            print(f"Error: {e}")

    # add multiple records
    @staticmethod
    def insert_table():
        sql = "INSERT INTO students(name, email, dept) VALUES (%s, %s, %s)"
        val = [
            ("ROHIT", "rohit@example.com", "CE"),
            ("VIRAT", "virat@example.com", "ME"),
            ("SACHIN", "sachin@example.com", "IT"),
            ("ABHISHEK", "abhishek@example.com", "EC"),
        ]
        cursor.executemany(sql, val)
        conn.commit()
        print(f"\n--- {cursor.rowcount} data inserted into table. ---")

    # fetch and print records
    @staticmethod
    def read_table():
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        for row in result:
            print(row)

    # update the data
    @staticmethod
    def update_table():
        sql = "UPDATE students SET name = %s, email = %s WHERE name = %s AND email = %s"
        val = ("YUVRAJ", "yuvraj@example.com", "ABHISHEK", "abhishek@example.com")
        cursor.execute(sql, val)
        conn.commit()
        print(f"\n--- {cursor.rowcount} row's updated. ---")

    # delete the data
    @staticmethod
    def delete_table():
        sql = "DELETE FROM students WHERE name = 'SACHIN'"
        cursor.execute(sql)
        conn.commit()
        print(f"\n--- {cursor.rowcount} data deleted. ---")


def main():
    # sequence of operations to demonstrate the CRUD operations
    StudentInfo.create_table()
    StudentInfo.insert_table()
    StudentInfo.read_table()

    StudentInfo.update_table()
    StudentInfo.read_table()

    StudentInfo.delete_table()
    StudentInfo.read_table()

    print(f"\n--- Total: {cursor.rowcount} data rows available. ---\n")


if __name__ == "__main__":
    main()
