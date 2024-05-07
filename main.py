import functions

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
            user_input = int(input(""))
            break
        except:
            functions.invalid_selection_msg()

    if user_input in menu_options:
        choice = user_input
    else:
        functions.invalid_selection_msg()

# Add new employee record to database
if choice == 1:
    new_employee = input("You have selected option 1. Please enter new employee details in following format:\n<Employee firstname>, <Employee lastname>, <Employee ID>, <Mobile number>, <Email address>, <Title>, <Remuneration>, <Employment status>\n")
    new_employee_list = new_employee.split(", ")
    firstname, lastname, id, mobile, email, title, remuneration, employment_status = new_employee_list 

# # Remove existing employee record from database
# if option == "2":
#     print("Please enter employee ID of employee whose records you wish to remove from database")

# # Modify existing employee record
# if option == "3":
#     print("Please enter employee ID of employee whose records who wish to modify")
