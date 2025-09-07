class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        print("Animal makes some sound...")

    def feed(self):
        print(f"{self.name} est edu")

animal = Animal("noname", "3")
print(f"{animal.name}, {animal.age} лет")
animal.make_sound()        

class Lion(Animal):
    def make_sound(self):
        print("Roar!")
    
    def feed(self):
        print(f"{self.name} est doner")
    
    
class Monkey(Animal):
    def make_sound(self):
        print("Уу аа")

    def feed(self):
        print(f"{self.name} est banana")

class Elephant(Animal):
    def make_sound(self):
        print("Uuuuuu")
    
    def feed(self):
        print(f"{self.name} est travu")


class Zoo:
    def __init__(self):
        self.animals = []
    
    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} added to zoo")

    def show_all(self):
        for animal in self.animals:
            print(f"{animal.name}, {animal.age} vozsrat")
    
    def make_all_sound(self):
        for animal in self.animals:
            animal.make_sound()

lion = Lion("Yerassyl", 18)
monkey = Monkey("Aknazar", 15)
elephant = Elephant("Persidskiy", 15)

lion.make_sound()
monkey.make_sound()
elephant.make_sound()

lion.feed()
monkey.feed()
elephant.feed()

zoo = Zoo()

zoo.add_animal(lion)
zoo.add_animal(monkey)
zoo.add_animal(elephant)

zoo.show_all()

zoo.make_all_sound()

