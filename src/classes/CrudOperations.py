# library imports
import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract

# local import
from Student import Student


# CRUD operations
class StudentInfo:

    # create students table
    @staticmethod
    def create_table(conn: MySQLConnectionAbstract) -> None:
        with conn.cursor() as cursor:
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
            except mysql.connector.Error as e:
                print(f"Error: {e}")

    # add multiple records
    @staticmethod
    def insert_table(conn: MySQLConnectionAbstract, students: list[Student]) -> None:
        with conn.cursor() as cursor:
            sql: str = "INSERT INTO students(name, email, dept) VALUES (%s, %s, %s)"
            val: list[tuple[str, str, str]] = [
                (s.name, s.email, s.dept) for s in students
            ]
            cursor.executemany(sql, val)
            conn.commit()
            print(f"\n--- {cursor.rowcount} data inserted into table. ---")

    # fetch and print records
    @staticmethod
    def read_table(conn: MySQLConnectionAbstract) -> list[Student]:
        with conn.cursor() as cursor:
            query: str = "SELECT name, email, dept FROM students"
            try:
                cursor.execute(query)
                rows = cursor.fetchall()
                students: list[Student] = [
                    Student(name=row[0], email=row[1], dept=row[2]) for row in rows
                ]
                return students

            except Exception as e:
                print(f"Error reading table: {e}")
                return []

    # update the data
    @staticmethod
    def update_table(
        conn: MySQLConnectionAbstract,
        new_student: Student,
        old_student: Student,
    ) -> None:
        with conn.cursor() as cursor:
            sql: str = (
                "UPDATE students SET name = %s, email = %s, dept = %s WHERE name = %s AND email = %s"
            )
            val: tuple[str, str, str, str, str] = (
                new_student.name,
                new_student.email,
                new_student.dept,
                old_student.name,
                old_student.email,
            )
            cursor.execute(sql, val)
            conn.commit()
            print(f"\n--- {cursor.rowcount} row's updated. ---")

    # delete the data
    @staticmethod
    def delete_table(conn: MySQLConnectionAbstract, student: Student) -> None:
        with conn.cursor() as cursor:
            sql: str = "DELETE FROM students WHERE name = %s AND email = %s"
            params: tuple[str, str] = (student.name, student.email)
            cursor.execute(sql, params)
            conn.commit()
            print(f"\n--- {cursor.rowcount} data deleted. ---")
