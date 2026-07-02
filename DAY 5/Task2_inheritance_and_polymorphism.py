class Employee:
    def calculate_salary(self):
        return 30000

class Developer(Employee):
    def calculate_salary(self):
        base_salary=super().calculate_salary()
        bonus=10000
        return base_salary+bonus

class Designer(Employee):
    def calculate_salary(self):
            base_salary=super().calculate_salary()
            bonus=5000
            return base_salary+bonus

developer=Developer()
designer=Designer()

print("Developer Salary:",developer.calculate_salary())
print("Designer Salary:",designer.calculate_salary())