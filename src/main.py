from classes.Student import Student
from classes.Config import Config
import mysql.connector
import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

try:
    conn = Config.get_connection()
    cursor = conn.cursor()
except mysql.connector.Error as error:
    print(f"Error: {error}")
    exit(1)


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
        # Using the Student model for validation
        new_student = Student(name="ROHIT", email="rohit@example.com", dept="CE")

        val = [
            (new_student.name, new_student.email, new_student.dept),
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
    print("\nInitial Data:")
    StudentInfo.read_table()

    StudentInfo.update_table()
    print("\nInitial Data:")
    StudentInfo.read_table()

    StudentInfo.delete_table()
    print("\nInitial Data:")
    StudentInfo.read_table()

    print(f"\n--- Total: {cursor.rowcount} data rows available. ---\n")

    # Clean up
    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
