import csv
from colorama import Fore
import display_functions

def get_fields(employee_database="employee_database.csv"):
    fields_list = list()
    with open(employee_database) as f:
        data = f.readline()
        fields_list = data.strip("\n").split(",")
    return fields_list

def add_record(new_employee, employee_database="employee_database.csv"):
    with open(employee_database, "a") as f:
        writer = csv.DictWriter(f, fieldnames=new_employee.keys())
        writer.writerow(new_employee)

def remove_record(identification, employee_database="employee_database.csv"):
    lines = list()
    with open(employee_database, "r") as readfile:
        reader = csv.reader(readfile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == identification:
                    lines.remove(row)
    with open(employee_database, "w") as writefile:
        writer = csv.writer(writefile)
        writer.writerows(lines)

def update_record(identification, updated_field_index, updated_value, employee_database="employee_database.csv"):
    lines = list()
    with open(employee_database, "r") as readfile:
        reader = csv.reader(readfile)
        lines = list(reader)
        for row in lines:
            if identification in row:
                row[updated_field_index] = updated_value
    with open(employee_database, "w") as writefile:
        writer = csv.writer(writefile)
        writer.writerows(lines)

def print_record(identification, employee_database="employee_database.csv"):
    with open(employee_database) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["identification"] == identification:
                for field, value in row.items():
                    print("{}: {}".format(field.capitalize(), value))

def print_all_records(employee_database="employee_database.csv"):
    with open(employee_database) as f:
        reader = csv.reader(f)
        for row in reader:
            print("{:<15} {:<15} {:<15} {:<15} {:<30} {:<30} {:<15} {:<20}".format(*row))

def print_modified_record(identification, updated_field, updated_value, employee_database="employee_database.csv"):
    with open(employee_database) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["identification"] == identification:
                for field, value in row.items():
                    if field == updated_field:
                        value = updated_value
                    print(display_functions.Weight.bold + "{}: {}".format(field.capitalize(), value) + display_functions.Weight.reset)