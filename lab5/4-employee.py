class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Employee ID: {self.employee_id}\nName: {self.name}")


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id)
        self.salary = salary
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Position: Manager\nSalary: ${self.salary}\nDepartment: {self.department}")

    def manage_team(self):
        print("Manages the team and oversees projects.")


class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id)
        self.salary = salary
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Position: Engineer\nSalary: ${self.salary}\nProgramming Language: {self.programming_language}")

    def write_code(self):
        print("Writes code to develop software solutions.")


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id)
        self.salary = salary
        self.sales_target = sales_target

    def display_info(self):
        super().display_info()
        print(f"Position: Salesperson\nSalary: ${self.salary}\nSales Target: ${self.sales_target}")

    def meet_sales_target(self):
        print("Works to achieve and exceed sales targets.")


def main():
    manager = Manager("John Smith", "M001", 80000, "Marketing")
    manager.display_info()
    manager.manage_team()

    engineer = Engineer("Jane Doe", "E001", 70000, "Python")
    engineer.display_info()
    engineer.write_code()
    
    salesperson = Salesperson("Bob Johnson", "S001", 60000, 100000)
    salesperson.display_info()
    salesperson.meet_sales_target()


if __name__ == "__main__":
    main()
