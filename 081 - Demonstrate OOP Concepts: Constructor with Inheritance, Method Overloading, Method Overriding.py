# a. Constructor with inheritance
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Buddy", "Golden Retriever")
print(f"Name: {dog.name}, Breed: {dog.breed}")

# b. Method overloading
# Python does not support method overloading natively. However, you can achieve it using default arguments or variable-length arguments. Here's an example:
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(1, 2))  # 3
print(calc.add(1, 2, 3, 4))  # 10

# c. Method overriding
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

dog = Dog()
dog.sound()  # Output: Bark