import mysql.connector
from classes.Student import Student
from classes.DbConnections import DBConnection


# CRUD operations
class StudentInfo:
    conn = None
    cursor = None

    @classmethod
    def get_cursor(cls):
        if cls.conn is None or not cls.conn.is_connected():
            try:
                cls.conn = DBConnection.get_connection()
                cls.cursor = cls.conn.cursor()
            except mysql.connector.Error as error:
                print(f"Error connecting to database: {error}")
                exit(1)
        return cls.cursor, cls.conn

    # create students table
    @classmethod
    def create_table(cls):
        cursor, _ = cls.get_cursor()
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
    @classmethod
    def insert_table(cls, students: list[Student]):
        cursor, conn = cls.get_cursor()
        sql = "INSERT INTO students(name, email, dept) VALUES (%s, %s, %s)"
        val = [(s.name, s.email, s.dept) for s in students]
        cursor.executemany(sql, val)
        conn.commit()
        print(f"\n--- {cursor.rowcount} data inserted into table. ---")

    # fetch and print records
    @classmethod
    def read_table(cls):
        cursor, conn = cls.get_cursor()
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        for row in result:
            print(row)

    # update the data
    @classmethod
    def update_table(cls, new_student: Student, old_student: Student):
        cursor, conn = cls.get_cursor()
        sql = "UPDATE students SET name = %s, email = %s WHERE name = %s AND email = %s"
        val = (new_student.name, new_student.email, old_student.name, old_student.email)
        cursor.execute(sql, val)
        conn.commit()
        print(f"\n--- {cursor.rowcount} row's updated. ---")

    # delete the data
    @classmethod
    def delete_table(cls, student: Student):
        cursor, conn = cls.get_cursor()
        sql = "DELETE FROM students WHERE name = %s AND email = %s"
        cursor.execute(sql, (student.name, student.email))
        conn.commit()
        print(f"\n--- {cursor.rowcount} data deleted. ---")

    # closing a connection
    @classmethod
    def close_connection(cls):
        if cls.cursor:
            cls.cursor.close()
        if cls.conn and cls.conn.is_connected():
            cls.conn.close()
            print("\n--- Connection closed. ---")
