import csv
import add_employee
import remove_employee
import validation_functions

def print_line():
    print(75 * "-")

# Display menu selection options and prompt user for input until valid option is selected
def display_options(options:dict):
    print("\nWelcome to the employee database. Select from the following options:")
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
user_input = None
choice = None
while choice is None:
    while True:
        try:
            user_input = int(input())
            break
        except:
            validation_functions.selection_invalid_msg()
    if user_input in menu_options:
        choice = user_input
    else:
        validation_functions.selection_invalid_msg()

# Add new employee record to database
if choice == 1:
    # Prompt user to input employee details
    print(f"You have selected option 1: {menu_options[1]}. Please enter the new employee's:\n")
    firstname = add_employee.get_firstname()
    lastname = add_employee.get_lastname()
    id = add_employee.get_id()
    mobile = add_employee.get_mobile()
    email = add_employee.get_email()
    title = add_employee.get_title()
    remuneration = add_employee.get_remuneration()
    employment = add_employee.get_employment()

    # Create dict with new employee's details
    new_employee = {
        "firstname": firstname,
        "lastname": lastname,
        "id": id,
        "mobile": mobile,
        "email": email,
        "title": title,
        "remuneration": remuneration,
        "employment": employment
    }

    # Prompt user for confirmation
    print_line()
    for field, detail in new_employee.items():
        print("{}: {}".format(field.capitalize(), detail))
    print_line()

    while True:
        confirmation = input("Confirm the above details are correct (Y/N): ")
        if validation_functions.yn_validation(confirmation):
            break
        else:
            validation_functions.yn_invalid_msg()

    # Append new employee's record to database
    add_employee.add_record(new_employee)
    print("Employee record sucessfully added to database.")

# Remove existing employee record from database
if choice == 2:
    # Prompt user to input ID of employee whose records will be removed
    id = remove_employee.get_existing_id()
    print("")

    # Search database for employee ID, display existing records and prompt user for confirmation
    remove_employee.print_record(id)
    print_line()

    while True:
        confirmation = input("Confirm the above employee record to be removed (Y/N): ")
        if validation_functions.yn_validation(confirmation):
            break
        else:
            validation_functions.yn_invalid_msg()

    # Remove employee record from database
    remove_employee.remove_record(id)
    print("Employee record sucessfully removed from database.")