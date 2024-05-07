import validation_functions
from titles import titles

def get_firstname():
    while True:
        firstname = input("First name: ")
        if validation_functions.name_validation(firstname):
            break
        else:
            print("Invalid input, please enter a name containing letters only.")
    return firstname    

def get_lastname():
    while True:
        lastname = input("Last name: ")
        if validation_functions.name_validation(lastname):
            break
        else:
            print("Invalid input, please enter a name containing letters only.")
    return lastname

def get_id():
    while True:
        id = input("Employee ID: ")
        if validation_functions.id_validation(id):
            break
        else:
            print("Invalid input, please enter an employee ID that is numeric and six digits in length.")
    return id

def get_mobile():
    while True:
        mobile = str(input("Mobile: "))
        if validation_functions.mobile_validation(mobile):
            break
        else:
            print("Invalid input, please enter an mobile number that is numeric, 10 digits in length, and starts with '04'.")
    return mobile

def get_email():
    while True:
        email = input("Email: ")
        if validation_functions.email_validation(email):
            break
        else:
            print("Invalid input, please enter a valid email address.")
    return email

def get_title():
    while True:
        title = input("Title: ")
        if validation_functions.title_validation(title):
            break
        else:
            print("Invalid title, please enter a valid role. Valid roles:")
            print(*titles, sep = ", ")
    return title

def get_remuneration():
    while True:
        remuneration = input("Remuneration: ")
        try:
            val = int(remuneration)
            if val < 0:
                print("Invalid input, please enter a remuneration amount that is a positive integer.")
                continue
            break
        except:
            print("Invalid input, please enter a remuneration amount that is a positive integer.")
    return remuneration
    