import csv
import validation_functions

def get_firstname():
    while True:
        firstname = input("Firstname: ").capitalize()
        if validation_functions.name_validation(firstname):
            break
        else:
            print("Invalid input, enter a name containing letters only.")
    return firstname    

def get_lastname():
    while True:
        lastname = input("Lastname: ").capitalize()
        if validation_functions.name_validation(lastname):
            break
        else:
            print("Invalid input, enter a name containing letters only.")
    return lastname

def get_id():
    while True:
        id = input("Employee ID: ")
        if validation_functions.id_validation(id) and not validation_functions.id_exists(id):
            break
        else:
            print("Invalid input, enter an employee ID that is numeric, six digits in length, and does not already exist.")
    return id

def get_mobile():
    while True:
        mobile = str(input("Mobile: "))
        if validation_functions.mobile_validation(mobile):
            break
        else:
            print("Invalid input, enter an mobile number that is numeric, 10 digits in length, and starts with '04'.")
    return mobile

def get_email():
    while True:
        email = input("Email: ")
        if validation_functions.email_validation(email):
            break
        else:
            print("Invalid input, enter a valid email address.")
    return email

def get_title():
    while True:
        title = input("Title: ").capitalize()
        if validation_functions.title_validation(title):
            break
        print("Invalid title, enter a valid role from the following:")
        with open("titles.txt") as f:
            data = f.read()
            print(data.replace("\n", ", "))
    return title

def get_remuneration():
    while True:
        remuneration = input("Remuneration: ")
        try:
            val = int(remuneration)
            if val < 0:
                print("Invalid input, enter a remuneration amount that is a positive integer.")
                continue
            break
        except:
            print("Invalid input, enter a remuneration amount that is a positive integer.")
    return remuneration

def get_employment():
    while True:
            employment = input("Employment status: ").capitalize()
            if validation_functions.employment_validation(employment):
                break
            else:
                print("Invalid employment status, enter a valid employment status from the following:")
                with open("employment.txt") as f:
                    data = f.read()
                    print(data.replace("\n", ", "))
    return employment

def add_record(new_employee):
    with open('employee_database.csv', 'a') as f:
        writer = csv.DictWriter(f, fieldnames=new_employee.keys())
        writer.writerow(new_employee)