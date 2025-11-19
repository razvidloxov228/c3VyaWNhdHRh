class Animal:
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} ({self.species}, {self.age} років) каже: {self.sound}")
cat = Animal("Нявчик", "кіт", 3, "Няв!")
dog = Animal("Цербер", "собака", 5, "Гав!")
cat.make_sound()
dog.make_sound()
