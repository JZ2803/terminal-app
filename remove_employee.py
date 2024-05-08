import csv
import validation_functions

def get_existing_id():
    while True:
        id = input("Enter employee ID of employee whose record will be removed: ").capitalize()
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
                for field, detail in row.items():
                    print("{}: {}".format(field.capitalize(), detail))

def remove_record(id):
    lines = list()
    with open("employee_database.csv", "r") as readfile:
        reader = csv.reader(readfile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == id:
                    lines.remove(row)
    with open("employee_database.csv", "w") as writefile:
        writer = csv.writer(writefile)
        writer.writerows(lines)
