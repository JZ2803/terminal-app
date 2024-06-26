from colorama import Fore
import csv
import re

def selection_invalid_msg():
    print("Invalid input, select from displayed options.")

def name_validation(name):
    return name.isalpha()

def identification_validation(identification):
    return True if identification.isnumeric() and len(identification) == 6 else False

def identification_exists(identification, employee_database="employee_database.csv"):
    with open(employee_database) as f:
        reader = csv.DictReader(f)
        for row in reader:
            for key, value in row.items():
                if key == "identification" and value == str(identification):
                    return True
    return False

def get_existing_identification(prompt:str):
    while True:
        identification = input(prompt)
        if identification_exists(identification):
            break
        print("Invalid input, enter an existing employee ID.")
    return identification

def mobile_validation(mobile):
    return True if mobile.isnumeric() and len(mobile) == 10 and mobile[0:2] == '04' else False

def email_validation(email):
    return True if re.match(r"[^@]+@[^@]+\.[^@]+", email) else False

def title_validation(title, titles="titles.txt"):
    title_list = list()
    with open(titles) as f:
        for line in f:
            title_list.append(line.strip("\n"))
    return True if title in title_list else False

def remuneration_validation(remuneration):
    return True if remuneration > 0 else False

def employment_validation(employment, employment_types="employment_types.txt"):
    employment_list = list()
    with open(employment_types) as f:
        for line in f:
            employment_list.append(line.strip("\n"))
    return True if employment in employment_list else False
    
def confirmation_validation(prompt:str, feedback:str):
    while True:
        confirmation = input(prompt).upper()
        if confirmation == "Y":
            break
        if confirmation == "N":
            print(Fore.YELLOW + feedback + Fore.RESET)
            exit()
        print("Invalid input, enter Y or N.")