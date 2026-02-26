import sys
from pathlib import Path

# parent of src/ is on the python path so all modules can be imported correctly from the classes/ sub-package
ROOT_DIR: Path = Path(__file__).parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# ----- library import -----
from typing import List, Optional
from mysql.connector.connection import MySQLConnection

# ----- local import -----
from classes.Student import Student
from utils import get_db_connection


def main() -> None:
    conn: Optional[MySQLConnection] = get_db_connection()
    if not conn:
        return

    try:
        # ----- create table -----
        Student.create_table(conn)

        # ----- insert data into table -----
        students: List[Student] = [
            Student(name="ROHIT", email="rohit@example.com", dept="CE"),
            Student(name="VIRAT", email="virat@example.com", dept="ME"),
            Student(name="SACHIN", email="sachin@example.com", dept="IT"),
            Student(name="ABHISHEK", email="abhishek@example.com", dept="EC"),
        ]
        for s in students:
            s.save_data(conn)  # Using save_data instance method

        # ----- finding all data from table -----
        print(f"\n-> Current data in database table:")
        all_students = Student.find_all(conn)
        for s in all_students:
            print(f"ID: {s.id} | Name: {s.name} | Email: {s.email} | Dept: {s.dept}")

        # ----- update table data -----
        target_id = next((s.id for s in all_students if s.name == "ABHISHEK"), None)
        if target_id:
            student = Student.find_one(conn, target_id)
            if student:
                student.name = "YUVRAJ"
                student.email = "yuvraj@example.com"
                student.dept = "AIML"
                student.save_data(conn)
                print(
                    f"\n--- Updated student to: Name: {student.name} | Email: {student.email} | Dept: {student.dept} ---"
                )

        print("\n-> Updated Data:")
        all_students = Student.find_all(conn)
        for s in all_students:
            print(f"ID: {s.id} | Name: {s.name} | Email: {s.email} | Dept: {s.dept}")

        # ----- delete data from table -----
        target_delete = next((s for s in all_students if s.name == "SACHIN"), None)
        if target_delete:
            target_delete.delete_data(conn)

        print("\n-> Final Data:")
        for s in Student.find_all(conn):
            print(f"ID: {s.id} | Name: {s.name} | Email: {s.email} | Dept: {s.dept}")

    except Exception as e:
        print(f"Error during execution: {e}")

    finally:
        conn.close()
        print("\n--- Connection closed successfully. ---")


if __name__ == "__main__":
    main()
