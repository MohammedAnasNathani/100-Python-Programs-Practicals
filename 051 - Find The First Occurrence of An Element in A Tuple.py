my_tuple = (1, 2, 3, 4, 5, 6)
element = 4

if element in my_tuple:
    index = my_tuple.index(element)
    print(f"First occurrence of {element} is at index {index}")
else:
    print(f"{element} is not found in the tuple.")
