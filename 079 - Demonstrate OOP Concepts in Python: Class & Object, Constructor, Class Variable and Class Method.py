#  Class & Object
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"Car make: {self.make}, Model: {self.model}")

# Creating an object of the Car class
car = Car("Toyota", "Corolla")
car.display_info()

# b. Constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, I'm {self.name} and I am {self.age} years old.")

# Creating an object of the Person class
person = Person("John", 30)
person.introduce()

# c. Class variable and Class method
class Employee:
    company = "XYZ Inc."

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def get_company(cls):
        return cls.company

# Creating an object of the Employee class
emp = Employee("Alice", 50000)
print(f"Employee works at {emp.get_company()}")