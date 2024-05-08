import validation_functions
import add_employee
import sys
import csv

def print_line():
    print(75 * "-")

# Display menu selection options and prompt user for input until valid option is selected
def display_options(options:dict):
    print("\nWelcome to the employee database. Please select from the following options:")
    print_line()
    for option, description in options.items():
        print("{}: {}".format(option, description))
    print_line()

menu_options = {1: "Add new employee record to database",
                2: "Remove existing employee record from database",
                3: "Modify existing employee record",
                4: "View all employee records",
                5: "View a filtered list of employee records based on selection criteria"}

display_options(menu_options)
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
    # Prompt user to input employee details
    print(f"You have selected option 1: {menu_options[1]}. \nPlease enter the new employee's:\n")
    firstname = add_employee.get_firstname()
    lastname = add_employee.get_lastname()
    id = add_employee.get_id()
    mobile = add_employee.get_mobile()
    email = add_employee.get_email()
    title = add_employee.get_title()
    remuneration = add_employee.get_remuneration()
    employment = add_employee.get_employment()

    # Create list with new employee's details
    new_employee = [firstname, lastname, id, mobile, email, title, remuneration, employment]

    # Prompt user for confirmation
    print("Please confirm the following details are correct: Y/N")
    print(*new_employee, sep=", ")
    while True:
        confirmation = input()
        if validation_functions.yesno_validation(confirmation):
            break
        else:
            print("Invalid input, please enter Y or N.")

    # Write new employee's details to employee database file
    with open('employee_database.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(new_employee)