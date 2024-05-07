import re
from titles import titles

def invalid_selection_msg():
    print("Invalid selection, please select from displayed options.")

def name_validation(input):
    return input.isalpha()

def id_validation(input):
    return True if input.isnumeric() and len(input) == 6 else False

def mobile_validation(input):
    return True if input.isnumeric() and len(input) == 10 and input[0:2] == '04' else False

def email_validation(input):
    return True if re.match(r"[^@]+@[^@]+\.[^@]+", input) else False

def title_validation(input):
    return True if input in titles else False

def remuneration_validation(input):
    return True if input > 0 else False