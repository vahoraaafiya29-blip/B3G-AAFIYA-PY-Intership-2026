class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print("Brand:", self.brand,"|Model:",self.model,"|Year:",self.year)
    
car1=Car("Toyota","Fortuner",2022)
car2=Car("Hyundai","Creta",2023)
car3=Car("Honda","City",2021)

car1.display_info()
car2.display_info()
car3.display_info()
    