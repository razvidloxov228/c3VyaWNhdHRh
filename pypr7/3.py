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


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


def print_area(shape: Shape):
    """Функція приймає будь-яку фігуру та виводить її площу."""
    print(f"Площа: {shape.calculate_area():.2f}")


circle = Circle(7)
square = Square(4)
rectangle = Rectangle(3, 6)

print_area(circle)
print_area(square)
print_area(rectangle)
