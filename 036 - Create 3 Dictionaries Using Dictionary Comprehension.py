# Example 1: Create a dictionary with square of numbers
squares = {x: x ** 2 for x in range(1, 6)}
print("Squares dictionary:", squares)

# Example 2: Create a dictionary with even numbers
even_numbers = {x: x for x in range(2, 11, 2)}
print("Even numbers dictionary:", even_numbers)

# Example 3: Create a dictionary with key-value pairs as (number, its cube)
cubes = {x: x ** 3 for x in range(1, 6)}
print("Cubes dictionary:", cubes)
