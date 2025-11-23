from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    def total_area(self):
        return sum(shape.calculate_area() for shape in self.shapes)


circle = Circle(5)
rectangle = Rectangle(4, 6)

shapes = [circle, rectangle]

calculator = AreaCalculator(shapes)

print(f"Площа кола: {circle.calculate_area():.2f}")
print(f"Площа прямокутника: {rectangle.calculate_area():.2f}")
print(f"Загальна площа всіх фігур: {calculator.total_area():.2f}")
