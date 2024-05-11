import csv
import os
import pytest
import database_functions

test_employee = {
    "firstname": "Testo",
    "lastname": "Testerson",
    "identification": "123456",
    "mobile": "0400000000",
    "email": "test@email.com",
    "title": "Accountant",
    "remuneration": "120000",
    "employment": "Full-time"
    }

# Create test database file
test_database = "test_database.csv"

with open(test_database, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["firstname", "lastname", "identification", "mobile", "email", "title", "remuneration", "employment"])

# Database function tests
def test_get_fields():
    result = database_functions.get_fields()
    assert result == ["firstname", "lastname", "identification", "mobile", "email", "title", "remuneration", "employment"]

def test_add_record():
    database_functions.add_record(test_employee, test_database)
    
    with open(test_database, "r") as readfile:
        reader = csv.DictReader(readfile)
        assert test_employee in list(reader)

def test_remove_record():
    database_functions.remove_record("123456", test_database)

    with open(test_database, "r") as readfile:
        reader = csv.DictReader(readfile)
        for row in reader:
            assert row["identification"] != "123456"

def test_update_record():
    database_functions.add_record(test_employee, test_database)
    database_functions.update_record("123456", 5, "Finance manager", test_database)
    with open(test_database, "r") as readfile:
        reader = csv.DictReader(readfile)
        for row in reader:
            assert row == {
                "firstname": "Testo",
                "lastname": "Testerson",
                "identification": "123456",
                "mobile": "0400000000",
                "email": "test@email.com",
                "title": "Finance manager",
                "remuneration": "120000",
                "employment": "Full-time"
            }