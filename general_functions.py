import csv

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


