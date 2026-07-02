import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius *self.radius
    
    @property
    def circumference(self):
        return 2 * math.pi * self.radius
    

c1 = Circle(7)

print("Radius:",c1.radius)
print("Area:",round(c1.area,2))
print("Circumference:",round(c1.circumference,2))