# Display menu options
def display_options(options):
    print("\nWelcome to the employee database. Please select from the following options:")
    print(75 * "-")
    for option, description in options.items():
        print("{}: {}".format(option, description))
    print(75 * "-")

def invalid_selection_msg():
    print("Invalid selection, please select from displayed options.")