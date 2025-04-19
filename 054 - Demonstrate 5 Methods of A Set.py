my_set = {1, 2, 3, 4, 5}

# Method 1: add()
my_set.add(6)
print(f"After adding 6: {my_set}")

# Method 2: remove()
my_set.remove(2)
print(f"After removing 2: {my_set}")

# Method 3: discard()
my_set.discard(5)
print(f"After discarding 5: {my_set}")

# Method 4: clear()
my_set.clear()
print(f"After clearing the set: {my_set}")

# Method 5: union()
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(f"Union of sets: {union_set}")
