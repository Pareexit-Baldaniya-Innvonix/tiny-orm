import sys
from pathlib import Path
from classes.crud_operations import StudentInfo

# parent of src/ is on the python path so all modules can be imported correctly from the classes/ sub-package
ROOT_DIR = Path(__file__).parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))


def main():
    try:
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

    except Exception as error:
        print(f"Error: {error}")

    finally:
        # Clean up - close cursor and connection
        StudentInfo.close_connection()


if __name__ == "__main__":
    main()
