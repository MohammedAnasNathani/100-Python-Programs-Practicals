# a. Inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()

# b. Super method
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

child = Child("John", 5)
print(f"Name: {child.name}, Age: {child.age}")

# c. Polymorphism
class Bird:
    def sound(self):
        print("Tweet")

class Dog:
    def sound(self):
        print("Bark")

def make_sound(animal):
    animal.sound()

bird = Bird()
dog = Dog()

make_sound(bird)
make_sound(dog)