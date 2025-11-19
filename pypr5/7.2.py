class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Це {self.make} {self.model} {self.year} року виробництва.")


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def display_info(self):
        print(f"Автомобіль: {self.make} {self.model}, {self.year} рік. Паливо: {self.fuel_type}.")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_capacity):
        super().__init__(make, model, year)
        self.engine_capacity = engine_capacity

    def display_info(self):
        print(f"Мотоцикл: {self.make} {self.model}, {self.year} рік. Об'єм двигуна: {self.engine_capacity}cc.")


class Bicycle(Vehicle):
    def __init__(self, make, model, year, gear_count):
        super().__init__(make, model, year)
        self.gear_count = gear_count

    def display_info(self):
        print(f"Велосипед: {self.make} {self.model}, {self.year} рік. Кількість передач: {self.gear_count}.")


vehicles = [
    Car("Toyota", "Corolla", 2020, "бензин"),
    Motorcycle("Honda", "CBR600RR", 2019, 600),
    Bicycle("Trek", "Marlin 7", 2021, 10),
    Vehicle("Generic", "Transport", 2000)
]

for v in vehicles:
    v.display_info()
