import csv
import add_employee
import general_functions
import remove_employee
import validation_functions

def print_line():
    print(80 * "-")

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

# Menu option 1: Add new employee record to database
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

    validation_functions.confirmation_validation("Confirm the above details are correct (Y/N): ")

    # Append new employee's record to database
    add_employee.add_record(new_employee)
    print("Employee record sucessfully added to database.")

# Menu option 2: Remove existing employee record from database
if choice == 2:
    # Prompt user to input ID of employee whose records will be removed
    id = validation_functions.get_existing_id("Enter employee ID of employee whose record will be removed: ")
    print("")

    # Search database for employee ID, display existing records and prompt user for confirmation
    general_functions.print_record(id)
    print_line()
    validation_functions.confirmation_validation("Confirm the above employee record to be removed (Y/N): ")

    # Remove employee record from database
    remove_employee.remove_record(id)
    print("Employee record sucessfully removed from database.")

# Menu option 3: Modify existing employee record
if choice == 3:
    # Prompt user to input ID of employee whose records will be removed
    id = validation_functions.get_existing_id("Enter employee ID of employee whose record will be updated: ")
    print("")

    # Search database for employee ID, display existing records
    general_functions.print_record(id)
    print_line()
    
    # Prompt user to input field and value to update
    print("Enter field and new value to to update above employee record. E.g. 'Lastname: Smith'.")

    updated_record = str()
    fields_list = general_functions.get_fields()

    # While loop to continually prompt until a valid field/value is entered
    while True:
        try:
            updated_record = input("")
            updated_field = updated_record.split(": ")[0].lower()
            updated_field_index = fields_list.index(updated_field)
            updated_value = updated_record.split(": ")[1].capitalize()
        except:
            print("Invalid input, please try again.")
            continue

        if updated_field in fields_list:
            if updated_field == fields_list[0]:
                validation_functions.name_validation(updated_value)
                break
            if updated_field == fields_list[1]:
                validation_functions.name_validation(updated_value)
                break
            if updated_field == fields_list[2]:
                validation_functions.id_validation(updated_value)
                break
            if updated_field == fields_list[3]:
                validation_functions.mobile_validation(updated_value)
                break
            if updated_field == fields_list[4]:
                validation_functions.email_validation(updated_value)
                break
            if updated_field == fields_list[5]:
                validation_functions.title_validation(updated_value)
                break
            if updated_field == fields_list[6]:
                validation_functions.remuneration_validation(updated_value)
                break
            if updated_field == fields_list[7]:
                validation_functions.employment_validation(updated_value)
                break

        validation_functions.field_invalid_msg()
    
    # Modify employee record in database
    remove_employee.modify_record(id, updated_field_index, updated_value)
    print("Employee record sucessfully modified in database.")

# Menu option 4: View all employee records
if choice == 4:
    remove_employee.print_all_records()