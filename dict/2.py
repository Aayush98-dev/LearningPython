class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

d = Dog()
d.speak()

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog:
    # Class Attribute (shared)
    species = "Canine"

    # Constructor (initializes unique instance attributes)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Method (behavior)
    def bark(self):
        return f"{self.name} says Woof!"

# Creating an object (Instance)
my_dog = Dog("Buddy", 3)
print(my_dog.bark())  # Output: Buddy says Woof!



class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

animals = [Dog(), Cat()]

for a in animals:
    a.sound()

class Ride:
    def __init__(self, distance):
        self.distance = distance

    def fare(self):
        print("Base fare calculation")

class CarRide(Ride):   # inheritance
    def fare(self):
        print(self.distance * 10)

class BikeRide(Ride):  # inheritance
    def fare(self):
        print(self.distance * 5)

names = ["Zara", "Amit", "John"]
names.sort(key=lambda x: len(x))
print(names)