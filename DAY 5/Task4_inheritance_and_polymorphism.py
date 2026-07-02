class Bird:
     def fly(self):
          print("Bird is flying with wings")

class Airplane:
     def fly(self):
          print("airplane is flying with engine")

class Drone:
     def fly(self):
          print("Drone is flying with propellers")

def make_it_fly(obj):
     obj.fly()

make_it_fly(Bird())
make_it_fly(Airplane())
make_it_fly(Drone())                                  