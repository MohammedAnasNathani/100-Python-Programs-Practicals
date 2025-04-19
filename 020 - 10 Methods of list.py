my_list = [1, 2, 3, 4, 5]

# Append
my_list.append(6)
# Insert
my_list.insert(2, 10)
# Remove
my_list.remove(4)
# Pop
popped_value = my_list.pop()
# Extend
my_list.extend([7, 8])
# Sort
my_list.sort()
# Reverse
my_list.reverse()
# Count
count_of_10 = my_list.count(10)
# Index
index_of_10 = my_list.index(10)
# Clear
my_list.clear()

print(f"Updated List: {my_list}")
print(f"Popped Value: {popped_value}")
print(f"Count of 10: {count_of_10}")
print(f"Index of 10: {index_of_10}")
