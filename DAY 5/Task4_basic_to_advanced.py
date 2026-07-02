class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary
     
    def set_salary(self,new_salary):
        if new_salary>self.__salary:
            self.__salary=new_salary
            print("Salary Updated")
        else:
            print("Salary Cannot Decrease")

emp = Employee(30000)            

print("Current Salary:",
emp.get_salary())

emp.set_salary(35000)
print("Updated Salary:",
emp.get_salary())

emp.set_salary(25000)
print("Final Salary:",emp.get_salary())

         


