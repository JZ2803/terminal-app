import csv
import employee
import database_functions
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

menu_options = {
    1: "Add new employee record to database",
    2: "Remove existing employee record from database",
    3: "Update existing employee record",
    4: "View all employee records",
    5: "Search employee database"
}

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
    newEmployee = employee.Employee()
    newEmployee.setFirstname()
    newEmployee.setLastname()
    newEmployee.setIdentification()
    newEmployee.setMobile()
    newEmployee.setEmail()
    newEmployee.setTitle()
    newEmployee.setRemuneration()
    newEmployee.setEmployment()

    new_employee = newEmployee.__dict__

    # Prompt user for confirmation
    print_line()
    for field, detail in new_employee.items():
        print("{}: {}".format(field.capitalize(), detail))
    print_line()

    validation_functions.confirmation_validation("Confirm the above details are correct (Y/N): ", "No changes made.")

    # Append new employee's record to database
    database_functions.add_record(new_employee)
    print("Employee record sucessfully added to database.")

# Menu option 2: Remove existing employee record from database
if choice == 2:
    # Prompt user to input ID of employee whose records will be removed
    identification = validation_functions.get_existing_identification("Enter employee ID of employee whose record will be removed: ")
    print("")

    # Search database for employee ID, display existing records and prompt user for confirmation
    database_functions.print_record(identification)
    print_line()
    validation_functions.confirmation_validation("Confirm the above employee record to be removed (Y/N): ", "No changes made")

    # Remove employee record from database
    database_functions.remove_record(identification)
    print("Employee record sucessfully removed from database.")

# Menu option 3: Update existing employee record
if choice == 3:
    # Prompt user to input ID of employee whose records will be removed
    identification = validation_functions.get_existing_identification("Enter employee ID of employee whose record will be updated: ")
    print("")

    # Search database for employee ID, display existing records
    database_functions.print_record(identification)
    print_line()
    
    # Prompt user to input field and value to update
    print("Enter field and new value to update above employee record, e.g. 'Lastname: Smith'.")

    updated_record = str()
    fields_list = database_functions.get_fields()

    # While loop to continually prompt until a valid field/value is entered
    while True:
        try:
            updated_record = str(input(""))
            updated_field = updated_record.split(": ")[0].lower()
            updated_field_index = fields_list.index(updated_field)
            updated_value = updated_record.split(": ")[1].capitalize()
        except:
            print("Invalid input, enter valid field.")
            continue

        if updated_field in fields_list:
            match updated_field:
                case "firstname":
                    if validation_functions.name_validation(updated_value):
                        break
                case "lastname":
                    if validation_functions.name_validation(updated_value):
                        break
                case "identification":
                    if validation_functions.identification_validation(updated_value):
                        break
                case "mobile":
                    if validation_functions.mobile_validation(updated_value):
                        break
                case "email":
                    if validation_functions.email_validation(updated_value):
                        break
                case "title":
                    if validation_functions.title_validation(updated_value):
                        break
                case "remuneration":
                    if validation_functions.remuneration_validation(updated_value):
                        break
                case "employment":
                    if validation_functions.employment_validation(updated_value):
                        break
            
        print("Invalid input, enter valid field and value.")
    
    # Prompt user for confirmation
    print("")
    database_functions.print_modified_record(identification, updated_field, updated_value)
    print_line()
    validation_functions.confirmation_validation("Confirm updated employee record above (Y/N): ", "No changes made.")

    # Update employee record in database
    database_functions.update_record(identification, updated_field_index, updated_value)
    print("Employee record sucessfully updated in database.")

# Menu option 4: View all employee records
if choice == 4:
    print("\nDisplaying all employee records:\n")
    database_functions.print_all_records()
    print_line()

# Menu option 5: Search employee database
if choice == 5:
     # Prompt user to input field and value to update
    print("Enter field and value to search employee database, e.g. 'Employment: Casual'.")

    search_record = str()
    fields_list = database_functions.get_fields()

    # While loop to continually prompt until a valid field/value is entered
    while True:
        try:
            search_record = str(input(""))
            search_field = search_record.split(": ")[0].lower()
            search_field_index = fields_list.index(search_field)
            search_value = search_record.split(": ")[1].capitalize()
        except:
            print("Invalid input, enter valid field.")
            continue

        ## search and display if any  records match the value searched for
        
        lines = list()
        with open("employee_database.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[search_field_index] == search_value:
                    lines.append(row)
        if not lines:
            print("No records found matching input field and value.")
        else:
            print(f"\nDisplaying records matching -> {search_field}: {search_value}\n")
            print("{:<15} {:15} {:<15} {:<15} {:<30} {:<35} {:<15} {:<15}".format(*database_functions.get_fields()))
            for row in lines:
                print("{:<15} {:15} {:<15} {:<15} {:<30} {:<35} {:<15} {:<15}".format(*row))
        print_line()

        validation_functions.confirmation_validation("Would you like to make another search? (Y/N): ", "")