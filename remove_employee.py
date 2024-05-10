import csv

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

def update_record(id, updated_field_index, updated_value):
    lines = list()
    with open("employee_database.csv", "r") as readfile:
        reader = csv.reader(readfile)
        lines = list(reader)
        for row in lines:
            if id in row:
                lines[row.index(id)][updated_field_index] = updated_value
    with open("employee_database.csv", "w") as writefile:
        writer = csv.writer(writefile)
        writer.writerows(lines)

def print_all_records():
    with open("employee_database.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            print("{:<15} {:15} {:<15} {:<15} {:<30} {:<35} {:<15} {:<15}".format(*row))