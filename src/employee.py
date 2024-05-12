import validation_functions

class Employee():
    def __init__(self="", firstname="", lastname="", identification="", mobile="", email="", title="", remuneration="", employment=""):
        self.firstname = firstname
        self.lastname = lastname
        self.identification = identification
        self.mobile = mobile
        self.email = email
        self.title = title
        self.remuneration = remuneration
        self.employment = employment

    def setFirstname(self):
        while True:
            firstname = input("Firstname: ").capitalize()
            if validation_functions.name_validation(firstname):
                break
            else:
                print("Invalid input, enter a name containing letters only.")
        self.firstname = firstname

    def setLastname(self):
        while True:
            lastname = input("Lastname: ").capitalize()
            if validation_functions.name_validation(lastname):
                break
            else:
                print("Invalid input, enter a name containing letters only.")
        self.lastname = lastname

    def setIdentification(self):
        while True:
            identification = input("Employee ID: ")
            if validation_functions.identification_validation(identification) and not validation_functions.identification_exists(identification):
                break
            else:
                print("Invalid input, enter an employee ID that is numeric, six digits in length, and does not already exist.")
        self.identification = identification

    def setMobile(self):
        while True:
            mobile = str(input("Mobile: "))
            if validation_functions.mobile_validation(mobile):
                break
            else:
                print("Invalid input, enter an mobile number that is numeric, 10 digits in length, and starts with '04'.")
        self.mobile = mobile

    def setEmail(self):
        while True:
            email = input("Email: ")
            if validation_functions.email_validation(email):
                break
            else:
                print("Invalid input, enter a valid email address.")
        self.email = email

    def setTitle(self):
        while True:
            title = input("Title: ").capitalize()
            if validation_functions.title_validation(title):
                break
            print("Invalid title, enter a valid role from the following:")
            with open("titles.txt") as f:
                data = f.read()
                print(data.replace("\n", ", "))
        self.title = title

    def setRemuneration(self):
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
        self.remuneration = remuneration

    def setEmployment(self):
        while True:
                employment = input("Employment status: ").capitalize()
                if validation_functions.employment_validation(employment):
                    break
                else:
                    print("Invalid employment status, enter a valid employment status from the following:")
                    with open("employment_types.txt") as f:
                        data = f.read()
                        print(data.replace("\n", ", "))
        self.employment = employment