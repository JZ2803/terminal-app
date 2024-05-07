import functions
import validation_functions
import add_employee
import sys

def print_line():
    print(75 * "-")

# Display menu options
def display_options(options:dict):
    print("\nWelcome to the employee database. Please select from the following options:")
    print_line()
    for option, description in options.items():
        print("{}: {}".format(option, description))
    print_line()

# Display selection options and prompt user for input until valid option is selected
menu_options = {1: "Add new employee record to database",
                2: "Remove existing employee record from database",
                3: "Modify existing employee record",
                4: "View all employee records",
                5: "View a filtered list of employee records based on selection criteria"}

functions.display_options(menu_options)
user_input = 0
choice = None
while choice is None:
    while True:
        try:
            user_input = int(input())
            break
        except:
            validation_functions.invalid_selection_msg()

    if user_input in menu_options:
        choice = user_input
    else:
        validation_functions.invalid_selection_msg()

# Add new employee record to database
if choice == 1:
    print(f"\nYou have selected option 1: {menu_options[1]}. \nPlease enter the new employee's:")
    firstname = add_employee.get_firstname()
    lastname = add_employee.get_lastname()
    id = add_employee.get_id()
    mobile = add_employee.get_mobile()
    email = add_employee.get_email()
    title = add_employee.get_title()
    remuneration = add_employee.get_remuneration()
    # employment_status = input("Employment status: ")

    # new_employee = [firstname, lastname, id, mobile, email, title, remuneration, employment_status]

