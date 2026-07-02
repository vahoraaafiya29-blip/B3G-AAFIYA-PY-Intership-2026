class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area()== other.area()
    
r1 = Rectangle(4,6)
r2 = Rectangle(3,8)

print("Area of Rectangle 1:", r1.area())
print("Area of Rectangle 2:", r2.area())
print("Are Equal:",r1==r2)