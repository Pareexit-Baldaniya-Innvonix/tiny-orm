from pydantic import BaseModel
import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract
from typing import Optional


class Teacher(BaseModel):
    id: Optional[int] = None
    name: str
    email: str
    subject: str

    # CRUD Operations

    # ----- create table -----
    @staticmethod
    def create_table(conn: MySQLConnectionAbstract) -> None:
        with conn.cursor() as cursor:
            try:
                cursor.execute(
                    """ 
                    CREATE TABLE IF NOT EXISTS teacher(
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            name VARCHAR(255) NOT NULL,
                            email VARCHAR(255),
                            subject CHAR(255)
                            )
                    """
                )
                print(f"--- Table teacher created successfully ---\n")

            except mysql.connector.Error as error:
                print(f"Error creating table: {error}")

    # ----- inserting data -----
    @staticmethod
    def insert_data(conn: MySQLConnectionAbstract, teachers: list["Teacher"]) -> None:
        with conn.cursor() as cursor:
            try:
                query = "INSERT INTO teacher(name, email, subject) VALUES (%s, %s, %s)"
                value = [(t.name, t.email, t.subject) for t in teachers]
                cursor.executemany(query, value)
                conn.commit()
                print(f"--- {cursor.rowcount} data inserted. ---")

            except mysql.connector.Error as error:
                print(f"Error inserting data: {error}")

    # ----- read data from table -----
    @staticmethod
    def read_data(conn: MySQLConnectionAbstract) -> list["Teacher"]:
        with conn.cursor() as cursor:
            query = "SELECT id, name, email, subject FROM teacher"
            try:
                cursor.execute(query)
                rows = cursor.fetchall()
                teachers = [
                    Teacher(id=row[0], name=row[1], email=row[2], subject=row[3])
                    for row in rows
                ]
                return teachers

            except mysql.connector.Error as error:
                print(f"Error reading data: {error}")

    # ----- finding all teachers -----
    @staticmethod
    def find_all(
        conn: MySQLConnectionAbstract,
        criteria: Optional[dict] = None,
        order_by: Optional[str] = "name",
        direction: str = "ASC",
        limit: Optional[int] = None,
    ) -> list["Teacher"]:
        with conn.cursor() as cursor:
            try:
                query = f"SELECT id, name, email, subject FROM teacher"
                values = []

                if criteria:
                    conditions = [f"{key} = %s" for key in criteria.keys()]
                    query += " WHERE " + " AND ".join(conditions)
                    values = list(criteria.values())
                
                query += f" ORDER BY {order_by} {direction}"

                if limit is not None:
                    query += f" LIMIT {limit}"

                cursor.execute(query, values)
                rows = cursor.fetchall()

                return [
                    Teacher(id=row[0], name=row[1], email=row[2], subject=row[3])
                    for row in rows
                ]

            except mysql.connector.Error as error:
                print(f"Error finding all data: {error}")
                return []

    # ----- finding one perticulat data -----
    @staticmethod
    def find_one(
        conn: MySQLConnectionAbstract,
        criteria: Optional[dict] = None,
        order_by: Optional[str] = "name",
        direction: str = "ASC",
    ) -> Optional["Teacher"]:
        with conn.cursor() as cursor:
            try:
                conditions = " AND ".join([f"{key} = %s" for key in criteria.keys()])
                values = tuple(criteria.values())

                order = f" ORDER BY {order_by} {direction} " if order_by else ""
                sql = f"SELECT id, name, email, subject FROM teacher WHERE {conditions} {order} LIMIT 1"

                cursor.execute(sql, values)
                row = cursor.fetchone()

                if row:
                    return Teacher(id=row[0], name=row[1], email=row[2], subject=row[3])
                return None

            except mysql.connector.Error as error:
                print(f"Error finding one data: {error}")

    # ----- saving all data -----
    def save(self, conn: MySQLConnectionAbstract) -> None:
        with conn.cursor() as cursor:
            try:
                if self.id:
                    query: str = (
                        "UPDATE teacher SET name = %s, email = %s, subject = %s WHERE id = %s"
                    )
                    cursor.execute(
                        query, (self.name, self.email, self.subject, self.id)
                    )
                    action = "updated"
                else:
                    query: str = (
                        "INSERT INTO teacher(name, email, subject) VALUES (%s, %s, %s)"
                    )
                    cursor.execute(query, (self.name, self.email, self.subject))
                    self.id = cursor.lastrowid
                    action = "saved"

                conn.commit()
                print(f"--- Teacher {action} successfully. ---")

            except mysql.connector.Error as error:
                print(f"Error saving data: {error}")

    # ----- deleting record from table -----
    def delete(self, conn: MySQLConnectionAbstract):
        if not self.id:
            print(f"can't delete without teacher id.")
            return

        with conn.cursor() as cursor:
            try:
                query: str = "DELETE FROM teacher WHERE id = %s"
                cursor.execute(query, (self.id,))
                conn.commit()
                print(f"\n--- {cursor.rowcount} data deleted. ---")

            except mysql.connector.Error as error:
                print(f"Error deleting data: {error}")
