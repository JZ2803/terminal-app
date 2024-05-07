# Display menu options
def display_options(options):
    print("Welcome to the employee database. Please select from the following options:")
    for option, description in options.items():
        print("{}: {}".format(option, description))
