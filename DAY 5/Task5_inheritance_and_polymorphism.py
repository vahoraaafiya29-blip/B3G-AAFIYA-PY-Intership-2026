class vehicle:
    def __init__(self,brand):
     self.brand=brand

class Car(vehicle):
    def __init__(self,brand,model):
     super().__init__(brand)
     self.model=model 
    
class SportsCar(Car):
     def __init__(self,brand,model,speed):
      super().__init__(brand,model)
      self . speed= speed

     def show(self):
         print("Brand:",self.brand)
         print("Model:",self.model)
         print("Top Speed:",self.speed,"km/h")


car=SportsCar("Ferrari","F8",340)
car.show()       




    
