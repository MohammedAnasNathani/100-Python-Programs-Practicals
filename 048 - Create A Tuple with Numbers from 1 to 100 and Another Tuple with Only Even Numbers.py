numbers = tuple(range(1, 101))
even_numbers = tuple(x for x in numbers if x % 2 == 0)

print("Numbers from 1 to 100:", numbers)
print("Even numbers:", even_numbers)
