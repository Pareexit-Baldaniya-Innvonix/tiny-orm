import os
import sys
from classes.crud_operations import StudentInfo

# parent of src/ is on the python path so all modules can be imported correctly from the classes/ sub-package
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)


def main():
    # create table
    StudentInfo.create_table()

    # insert data into table
    StudentInfo.insert_table()
    print("\nInitial Data:")
    StudentInfo.read_table()

    # update table data
    StudentInfo.update_table()
    print("\nUpdated Data:")
    StudentInfo.read_table()

    # delete data from table
    StudentInfo.delete_table()
    print("\nFinal Data:")
    StudentInfo.read_table()

    # Clean up - close cursor and connection
    StudentInfo.close_connection()


if __name__ == "__main__":
    main()
