class Employee:
    nn = 100

    # constructor
    # def __init__(self, name, age, address, organization, designation):
    #     self.name = name
    #     self.age = age
    #     self.address = address
    #     self.organization = organization
    #     self.designation = designation

    # def __int__(self):
    #     print("Default")

    # properties of the class
    name = "Vikash Ravi Das"
    age = 21
    address = "Bhopal"
    designation = "Developer"
    organization = "Google"

    def display_data(self):
        # self is the keyword which is used to take the current instance
        print(self.name, self.age, self.organization, self.address)


# making object for the class
# object name            Class name
# employee       =      Employee()
# name = input("Enter the name: ")
# age = int(input("Enter the age: "))
# address = input("Enter the address: ")
# organization = input("Enter the company name")
# designation = input("Enter the Designation: ")
# employee = Employee(name, age, address, organization, designation)
# print(employee.name, employee.age, employee.address, employee.organization, employee.designation)
# print(employee)

"""
TODO: WHY WE ARE NOT ABLE TO ACCESS THIS???
emp1 = Employee()
print(emp1.nn)
"""


# emp1 = Employee()
# print(emp1.nn)
# employee.display_data()


# single level Inheritance

class Programmer(Employee):
    def about_program(self):
        print("I am a programmer")


programmer = Programmer()
programmer.name="Vikash Ravi Das"
print(programmer.name)
print(programmer.display_data())
