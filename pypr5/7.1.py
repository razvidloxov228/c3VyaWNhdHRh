class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        print(f"{self.make} {self.model}: Двигун запущено, врум! Паливо: {self.fuel_type}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, engine_capacity):
        super().__init__(make, model, year)
        self.engine_capacity = engine_capacity

    def rev_engine(self):
        print(f"{self.make} {self.model}: Реве двигун {self.engine_capacity}cc, брбрбр!")


class Bicycle(Vehicle):
    def __init__(self, make, model, year, gear_count):
        super().__init__(make, model, year)
        self.gear_count = gear_count

    def ring_bell(self):
        print(f"{self.make} {self.model}: Дзень-дзелень! Має {self.gear_count} передач.")


car = Car("Toyota", "Corolla", 2020, "бензин")
motorcycle = Motorcycle("Honda", "CBR600RR", 2019, 600)
bicycle = Bicycle("Trek", "Marlin 7", 2021, 10)

car.display_info()
car.start_engine()

motorcycle.display_info()
motorcycle.rev_engine()

bicycle.display_info()
bicycle.ring_bell()
