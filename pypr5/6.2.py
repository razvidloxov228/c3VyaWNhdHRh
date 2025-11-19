class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height
rect1 = Rectangle(5, 10)
rect2 = Rectangle(7, 3)
print(f"Прямокутник 1: ширина = {rect1.width}, висота = {rect1.height}, площа = {rect1.calculate_area()}")
print(f"Прямокутник 2: ширина = {rect2.width}, висота = {rect2.height}, площа = {rect2.calculate_area()}")
