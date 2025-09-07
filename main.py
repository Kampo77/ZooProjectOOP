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

lion = Lion("Yerassyl", 18)
monkey = Monkey("Aknazar", 15)
elephant = Elephant("Persidskiy", 15)

lion.make_sound()
monkey.make_sound()
elephant.make_sound()

lion.feed()
monkey.feed()
elephant.feed()