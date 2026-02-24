import sys
from pathlib import Path

# parent of src/ is on the python path so all modules can be imported correctly from the classes/ sub-package
ROOT_DIR = Path(__file__).parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from classes.CrudOperations import StudentInfo
from classes.Student import Student
from utils import get_db_connection


def main():
    students = [
        Student(name="ROHIT", email="rohit@example.com", dept="CE"),
        Student(name="VIRAT", email="virat@example.com", dept="ME"),
        Student(name="SACHIN", email="sachin@example.com", dept="IT"),
        Student(name="ABHISHEK", email="abhishek@example.com", dept="EC"),
    ]

    old_student = Student(name="ABHISHEK", email="abhishek@example.com", dept="EC")
    new_student = Student(name="YUVRAJ", email="yuvraj@example.com", dept="EC")
    delete_student = Student(name="SACHIN", email="sachin@example.com", dept="IT")

    conn = get_db_connection()
    if not conn:
        return

    cursor = conn.cursor()

    # create table
    try:
        StudentInfo.create_table(cursor)

    except Exception as e:
        print(f"Error creating a table: {e}")

    # insert data into table
    try:
        StudentInfo.insert_table(cursor, conn, students)
        print("\n-> Initial Data:")
        all_students = StudentInfo.read_table(cursor)
        for s in all_students:
            print(f"Student: {s.name}| Dept: {s.dept} | Email: {s.email} ")

    except Exception as e:
        print(f"Error during inserting data: {e}")

    # update table data
    try:
        StudentInfo.update_table(cursor, conn, new_student, old_student)
        print("\n-> Updated Data:")
        all_students = StudentInfo.read_table(cursor)
        for s in all_students:
            print(f"Student: {s.name}| Dept: {s.dept} | Email: {s.email} ")

    except Exception as e:
        print(f"Error updating table data: {e}")

    # delete data from table
    try:
        StudentInfo.delete_table(cursor, conn, delete_student)
        print("\n-> Final Data:")
        all_students = StudentInfo.read_table(cursor)
        for s in all_students:
            print(f"Student: {s.name}| Dept: {s.dept} | Email: {s.email} ")

    except Exception as e:
        print(f"Error deleting table data: {e}")

    cursor.close()
    conn.close()
    print("\n--- Connection closed successfully. ---")


if __name__ == "__main__":
    main()
