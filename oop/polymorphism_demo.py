import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, width, length):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle(width={self.length}, length={self.width})"

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle(radius={self.radius})"

    def area(self):
        return 3.14 * (self.radius ** 2)