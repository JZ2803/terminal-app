import csv

def add_record(new_employee):
    with open("employee_database.csv", "a") as f:
        writer = csv.DictWriter(f, fieldnames=new_employee.keys())
        writer.writerow(new_employee)

def update_record(identification, updated_field_index, updated_value):
    lines = list()
    with open("employee_database.csv", "r") as readfile:
        reader = csv.reader(readfile)
        lines = list(reader)
        for row in lines:
            if identification in row:
                row[updated_field_index] = updated_value
    with open("employee_database.csv", "w") as writefile:
        writer = csv.writer(writefile)
        writer.writerows(lines)

def print_record(identification):
    with open("employee_database.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["identification"] == identification:
                for field, value in row.items():
                    print("{}: {}".format(field.capitalize(), value))

def print_all_records():
    with open("employee_database.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            print("{:<15} {:15} {:<15} {:<15} {:<30} {:<35} {:<15} {:<15}".format(*row))

def print_modified_record(identification, updated_field, updated_value):
    with open("employee_database.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["identification"] == identification:
                for field, value in row.items():
                    if field == updated_field:
                        value = updated_value
                    print("{}: {}".format(field.capitalize(), value))

def get_fields():
    fields_list = list()
    with open("employee_database.csv") as f:
        data = f.readline()
        fields_list = data.strip("\n").split(",")
    return fields_list

def remove_record(identification):
    lines = list()
    with open("employee_database.csv", "r") as readfile:
        reader = csv.reader(readfile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == identification:
                    lines.remove(row)
    with open("employee_database.csv", "w") as writefile:
        writer = csv.writer(writefile)
        writer.writerows(lines)