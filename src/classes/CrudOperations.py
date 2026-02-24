import mysql.connector
from classes.Student import Student
from classes.DbConnections import DBConnection


# CRUD operations
class StudentInfo:
    conn = None
    cursor = None

    @staticmethod
    def get_cursor():
        if StudentInfo.conn is None or not StudentInfo.conn.is_connected():
            try:
                StudentInfo.conn = DBConnection.get_connection()
                StudentInfo.cursor = StudentInfo.conn.cursor()
            except mysql.connector.Error as error:
                print(f"Error connecting to database: {error}")
                exit(1)

        if StudentInfo.cursor is None:
            StudentInfo.cursor = StudentInfo.conn.cursor()

        return StudentInfo.cursor, StudentInfo.conn

    # create students table
    @staticmethod
    def create_table():
        cursor, _ = StudentInfo.get_cursor()
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
    def insert_table(students: list[Student]):
        cursor, conn = StudentInfo.get_cursor()
        sql = "INSERT INTO students(name, email, dept) VALUES (%s, %s, %s)"
        val = [(s.name, s.email, s.dept) for s in students]
        cursor.executemany(sql, val)
        conn.commit()
        print(f"\n--- {cursor.rowcount} data inserted into table. ---")

    # fetch and print records
    @staticmethod
    def read_table():
        cursor, conn = StudentInfo.get_cursor()
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        for row in result:
            print(row)

    # update the data
    @staticmethod
    def update_table(new_student: Student, old_student: Student):
        cursor, conn = StudentInfo.get_cursor()
        sql = "UPDATE students SET name = %s, email = %s, dept = %s WHERE name = %s AND email = %s"
        val = (new_student.name, new_student.email, new_student.dept, old_student.name, old_student.email)
        cursor.execute(sql, val)
        conn.commit()
        print(f"\n--- {cursor.rowcount} row's updated. ---")

    # delete the data
    @staticmethod
    def delete_table(student: Student):
        cursor, conn = StudentInfo.get_cursor()
        sql = "DELETE FROM students WHERE name = %s AND email = %s"
        cursor.execute(sql, (student.name, student.email))
        conn.commit()
        print(f"\n--- {cursor.rowcount} data deleted. ---")

    # closing a connection
    @staticmethod
    def close_connection():
        if StudentInfo.cursor:
            StudentInfo.cursor.close()
        if StudentInfo.conn and StudentInfo.conn.is_connected():
            StudentInfo.conn.close()
            print("\n--- Connection closed. ---")
