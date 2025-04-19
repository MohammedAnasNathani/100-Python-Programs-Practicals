import math

def calculate_area_from_circumference():
    circumference = float(input("Enter the circumference of the circle: "))
    radius = circumference / (2 * math.pi)
    area = math.pi * (radius ** 2)
    print(f"Area of the circle: {area}")

calculate_area_from_circumference()
