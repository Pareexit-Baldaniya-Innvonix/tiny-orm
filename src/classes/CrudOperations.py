import mysql.connector
from classes.Student import Student


# CRUD operations
class StudentInfo:

    # create students table
    @staticmethod
    def create_table(cursor):
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
    def insert_table(cursor, conn, students: list[Student]):
        sql = "INSERT INTO students(name, email, dept) VALUES (%s, %s, %s)"
        val = [(s.name, s.email, s.dept) for s in students]
        cursor.executemany(sql, val)
        conn.commit()
        print(f"\n--- {cursor.rowcount} data inserted into table. ---")

    # fetch and print records
    @staticmethod
    def read_table(cursor):
        query = "SELECT name, email, dept FROM students"
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            students = [Student(name=row[0], email=row[1], dept=row[2]) for row in rows]
            return students

        except Exception as e:
            print(f"Error reading table: {e}")
            return []

    # update the data
    @staticmethod
    def update_table(cursor, conn, new_student: Student, old_student: Student):
        sql = "UPDATE students SET name = %s, email = %s, dept = %s WHERE name = %s AND email = %s"
        val = (
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
    def delete_table(cursor, conn, student: Student):
        sql = "DELETE FROM students WHERE name = %s AND email = %s"
        cursor.execute(sql, (student.name, student.email))
        conn.commit()
        print(f"\n--- {cursor.rowcount} data deleted. ---")
