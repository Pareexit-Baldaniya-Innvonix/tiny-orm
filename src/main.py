import sys
from pathlib import Path

# parent of src/ is on the python path so all modules can be imported correctly from the classes/ sub-package
ROOT_DIR = Path(__file__).parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from classes.CrudOperations import StudentInfo
from classes.Student import Student


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

    # create table
    try:
        StudentInfo.create_table()
    except Exception as e:
        print(f"Error creating a table: {e}")

    # insert data into table
    try:
        StudentInfo.insert_table(students)
        print("\nInitial Data:")
        StudentInfo.read_table()
    except Exception as e:
        print(f"Error during inserting data: {e}")

    # update table data
    try:
        StudentInfo.update_table(new_student, old_student)
        print("\nUpdated Data:")
        StudentInfo.read_table()
    except Exception as e:
        print(f"Error updating table data: {e}")

    # delete data from table
    try:
        StudentInfo.delete_table(delete_student)
        print("\nFinal Data:")
        StudentInfo.read_table()
    except Exception as e:
        print(f"Error deleting table data: {e}")


if __name__ == "__main__":
    try:
        main()
    finally:
        StudentInfo.close_connection()  # destructor used to close corsor and connection
