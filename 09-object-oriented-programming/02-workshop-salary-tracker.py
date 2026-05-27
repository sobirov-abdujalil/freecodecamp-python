# Workshop: Build a Salary Tracker
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        return self.salary * 12

    def give_raise(self, percent):
        self.salary *= 1 + percent / 100

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, emp):
        self.employees.append(emp)

    def total_salary_budget(self):
        return sum(e.annual_salary() for e in self.employees)

emp = Employee("Bob", 5000)
dept = Department("Engineering")
dept.add_employee(emp)
print(f"Annual: ${emp.annual_salary():.2f}")
print(f"Dept budget: ${dept.total_salary_budget():.2f}")
