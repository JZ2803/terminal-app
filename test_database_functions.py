import csv
import database_functions
import employee
from display_functions import Weight

# Create test employee records
testEmployee1 = employee.Employee("Dwight", "Schrute", "123456", "0400000000", "dwight@email.com", "Sales specialist", "110000", "Full-time")
testEmployee2 = employee.Employee("Pam", "Beesly", "987654", "0499999999", "pam@email.com", "Administrative assistant", "85000", "Part-time")
testEmployee3 = employee.Employee("Angela", "Martin", "555555", "0412345678", "angela@email.com", "Finance manager", "150000", "Full-time")

test_employee_1 = testEmployee1.__dict__
test_employee_2 = testEmployee2.__dict__
test_employee_3 = testEmployee3.__dict__

# Create test database file
test_database = "test_database.csv"

with open(test_database, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["firstname", "lastname", "identification", "mobile", "email", "title", "remuneration", "employment"])

# Database function tests
class TestDatabaseFunctions:
    def test_get_fields(self):
        result = database_functions.get_fields()
        assert result == ["firstname", "lastname", "identification", "mobile", "email", "title", "remuneration", "employment"]

    def test_add_record(self):
        database_functions.add_record(test_employee_1, test_database)
        
        with open(test_database, "r") as readfile:
            reader = csv.DictReader(readfile)
            assert test_employee_1 in list(reader)

    def test_remove_record(self):
        database_functions.remove_record("123456", test_database)

        with open(test_database, "r") as readfile:
            reader = csv.DictReader(readfile)
            for row in reader:
                assert row["identification"] != "123456"

    def test_update_record(self):
        database_functions.add_record(test_employee_1, test_database)
        database_functions.update_record("123456", 5, "Chief executive officer", test_database)
        with open(test_database, "r") as readfile:
            reader = csv.DictReader(readfile)
            for row in reader:
                assert row == {
                    "firstname": "Dwight",
                    "lastname": "Schrute",
                    "identification": "123456",
                    "mobile": "0400000000",
                    "email": "dwight@email.com",
                    "title": "Chief executive officer",
                    "remuneration": "110000",
                    "employment": "Full-time"
                }

class TestTerminalOutput:
    def test_print_record(self, capsys):
        database_functions.print_record("123456", test_database)
        captured = capsys.readouterr()
        assert captured.out == "Firstname: Dwight\nLastname: Schrute\nIdentification: 123456\nMobile: 0400000000\nEmail: dwight@email.com\nTitle: Chief executive officer\nRemuneration: 110000\nEmployment: Full-time\n"

    def test_print_all_records(self, capsys):
        database_functions.add_record(test_employee_2, test_database)
        database_functions.add_record(test_employee_3, test_database)
        database_functions.print_all_records(test_database)
        captured = capsys.readouterr()
        assert captured.out == "firstname       lastname        identification  mobile          email                          title                          remuneration    employment          \nDwight          Schrute         123456          0400000000      dwight@email.com               Chief executive officer        110000          Full-time           \nPam             Beesly          987654          0499999999      pam@email.com                  Administrative assistant       85000           Part-time           \nAngela          Martin          555555          0412345678      angela@email.com               Finance manager                150000          Full-time           \n"

    def test_print_modified_record(self, capsys):
        database_functions.print_modified_record("987654", "remuneration", "90000", test_database)
        captured = capsys.readouterr()
        assert captured.out == "Firstname: Pam\nLastname: Beesly\nIdentification: 987654\nMobile: 0499999999\nEmail: pam@email.com\nTitle: Administrative assistant\nRemuneration: 90000\nEmployment: Part-time\n"