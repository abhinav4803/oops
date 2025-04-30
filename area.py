# CCreate a class reactangle with attribute la nd b and create method to compute area amd perimter
class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)

# Create a Rectangle object
rect = Rectangle(10, 5)

# Print area and perimeter
print("Area of rectangle:", rect.area())
print("Perimeter of rectangle:", rect.perimeter())
