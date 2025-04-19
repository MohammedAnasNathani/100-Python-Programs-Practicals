import math

def calculate_area():
    shape = input("Choose a shape (rectangle, circle, triangle): ").lower()
    
    if shape == "rectangle":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length * width
        print(f"Area of rectangle: {area}")
    
    elif shape == "circle":
        radius = float(input("Enter the radius: "))
        area = math.pi * (radius ** 2)
        print(f"Area of circle: {area}")
    
    elif shape == "triangle":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        area = 0.5 * base * height
        print(f"Area of triangle: {area}")
    
    else:
        print("Invalid shape.")

calculate_area()
