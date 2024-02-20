# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   Sarah Trostle,2/19/2024,Created Script
# ------------------------------------------------------------------------------------------ #
import json
import io as _io

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
message: str = ''  # Holds a custom message string.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
json_data: str = ''  # Holds combined string data in a json format.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
def read_data_from_file():
        global FILE_NAME
        global students

        try:
                file = open(FILE_NAME, "r")
                students = json.load(file)
                file.close()
        except FileNotFoundError as e:
                print("Text file must exist before running this script!\n")
                print("-- Technical Error Message -- ")
                print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
                print("There was a non-specific error!\n")
                print("-- Technical Error Message -- ")
                print(e, e.__doc__, type(e), sep='\n')
        finally:
                if file.closed == False:
                        file.close()


def output_menu():
    '''This function will print the menu options'''
    global MENU

    print(MENU)

def input_menu_choice():
    """This function takes the users input for the menu choice"""
    global menu_choice
    menu_choice = input("Enter your menu choice number: ")
    print()  # Adding extra space to make it look nicer.

def output_student_courses():
        '''This function displays the students current registrations'''
        global students

        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)
        

    # Input user data


def input_student_data():
        '''This function takes in student data to save to a JSON file'''
        global student_first_name
        global student_last_name
        global student_data
        global students

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            print(e)  # Prints the custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("Error: There was a problem with your entered data.")
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())

# write data to file

def write_data_to_file():
        '''This function writes the data inputted to a json file'''
        global file
        global students

try:
        file = open(FILE_NAME, "w")
        json.dump(students, file)
        file.close()
except TypeError as e:
        print("Please check that the data is a valid JSON format\n")
        print("-- Technical Error Message -- ")
        print(e, e.__doc__, type(e), sep='\n')
except Exception as e:
        print("-- Technical Error Message -- ")
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')
finally:
        if file.closed == False:
            file.close()

# read data
read_data_from_file()

#Loop through choices
while True:

    output_menu()
    input_menu_choice()

    if menu_choice == "1":
        input_student_data()
        continue 

    elif menu_choice == "2":
        output_student_courses()
        continue

    elif menu_choice == "3":
        write_data_to_file()
        continue

    elif menu_choice == "4":
        break  # out of the while loop

print("Program Ended")

