import csv
import re
import general_functions

# Functions for user input validation
def selection_invalid_msg():
    print("Invalid selection, select from displayed options.")

def field_invalid_msg():
    print("Invalid input, please enter valid field.")

def name_validation(input):
    return input.isalpha()

def id_validation(input):
    return True if input.isnumeric() and len(input) == 6 else False

def id_exists(input):
    fields_list = general_functions.get_fields()
    with open("employee_database.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if input == row[fields_list.index("id")]:
                return True
        return False

def get_existing_id(prompt:str):
    while True:
        id = input(prompt)
        if id_exists(id):
            break
        print("Invalid input, enter an existing employee ID.")
    return id

def mobile_validation(input):
    return True if input.isnumeric() and len(input) == 10 and input[0:2] == '04' else False

def email_validation(input):
    return True if re.match(r"[^@]+@[^@]+\.[^@]+", input) else False

def title_validation(input):
    title_list = list()
    with open("titles.txt") as f:
        for line in f:
            title_list.append(line.strip("\n"))
    return True if input in title_list else False

def remuneration_validation(input):
    return True if input > 0 else False

def employment_validation(input):
    employment_list = list()
    with open("employment.txt") as f:
        for line in f:
            employment_list.append(line.strip("\n"))
    return True if input in employment_list else False
    
def yn_validation(input):
    return True if input == 'Y' or 'N' else False

def confirmation_validation(prompt:str):
    while True:
        confirmation = input(prompt)
        if yn_validation(confirmation):
            if confirmation == "Y":
                break
            print("No changes made.")
            exit()
        else:
            print("Invalid input, please enter Y or N.")