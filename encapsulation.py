#  Below Employee class is the encapsulated class
class Employee:
    # defining the constructor for this class
    _name = "Imran Hasmi"

    def __init__(self, emp_id, emp_name, emp_designation):
        self.employee_id = emp_id
        self.employee_name = emp_name
        self.employee_designation = emp_designation

    def display(self):
        print(f"ID: {self.employee_id}\n"
              f"Name: {self.employee_name}\n"
              f"Designation: {self.employee_designation}")


emp = Employee("001", "Vikash", "Developer")

emp.

class Developer(Employee):
    def __int__(self, is_backend, developer_id):
        self.is_backend_developer = is_backend
        self.developer_id = developer_id
        super().__init__(emp_id=self.employee_id, emp_name=self.employee_name,
                         emp_designation=self.employee_designation)

    def display_developer_data(self):
        print(f"ID: {self.employee_id}\n"
              f"Name: {self.employee_name}\n"
              f"Designation: {self.employee_designation}\n"
              f"is Developer: {self.is_backend_developer}\n"
              f"developer id: {self.developer_id}")

# developer_object = Developer("001", "Vikash", "Developer")
# developer_object.__int__(True, "110")
#
# developer_object.display_developer_data()
