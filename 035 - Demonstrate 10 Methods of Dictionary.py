my_dict = {"name": "Alice", "age": 30, "city": "Paris"}

# Get value for key
print("Get value for 'name':", my_dict.get("name"))

# Add a new key-value pair
my_dict["country"] = "France"
print("After adding a new key:", my_dict)

# Update a value
my_dict["age"] = 31
print("After updating age:", my_dict)

# Remove a key-value pair
my_dict.pop("city")
print("After removing 'city':", my_dict)

# Get all keys
print("All keys:", my_dict.keys())

# Get all values
print("All values:", my_dict.values())

# Get all items (key-value pairs)
print("All items:", my_dict.items())

# Check if a key exists
print("Does 'name' exist in dictionary?", "name" in my_dict)

# Clear the dictionary
my_dict.clear()
print("After clearing:", my_dict)

# Copy the dictionary
my_dict = {"name": "Bob", "age": 40}
new_dict = my_dict.copy()
print("Copied dictionary:", new_dict)
