class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def make_sound(self):
        print("Animal makes some sound...")

animal = Animal("noname", "3")
print(f"{animal.name}, {animal.age} лет")
animal.make_sound()        