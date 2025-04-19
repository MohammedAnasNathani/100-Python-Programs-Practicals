def convert_temperature():
    temp = float(input("Enter temperature: "))
    unit = input("Is the temperature in Celsius (C) or Fahrenheit (F)? ").upper()
    
    if unit == 'C':
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}°C is equal to {fahrenheit}°F")
    elif unit == 'F':
        celsius = (temp - 32) * 5/9
        print(f"{temp}°F is equal to {celsius}°C")
    else:
        print("Invalid unit.")

convert_temperature()
