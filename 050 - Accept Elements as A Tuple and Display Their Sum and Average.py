elements = tuple(map(int, input("Enter numbers separated by space: ").split()))

total = sum(elements)
average = total / len(elements)

print("Sum:", total)
print("Average:", average)
