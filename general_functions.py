import csv
import validation_functions

def get_existing_id(prompt:str):
    while True:
        id = input(prompt)
        if validation_functions.id_exists(id):
            break
        else:
            print("Invalid input, enter an existing employee ID.")
    return id

def print_record(id):
    with open("employee_database.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['id'] == id:
                for field, value in row.items():
                    print("{}: {}".format(field.capitalize(), value))

def get_fields():
    fields_list = list()
    with open("employee_database.csv") as f:
        data = f.readline()
        fields_list = data.strip("\n").split(",")
    return fields_list