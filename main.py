import functions

# Display welcome and selection options and prompt user for input
menu_options = {1: "Add new employee record to database",
                2: "Remove existing employee record from database",
                3: "Modify existing employee record",
                4: "View all employee records",
                5: "View a filtered list of employee records based on selection criteria"}

functions.display_options(menu_options)
choice = None
while choice is None:
    user_input = int(input(""))
    if user_input in menu_options:
        choice = user_input
    else:
        print("Invalid selection, please select from available options.")