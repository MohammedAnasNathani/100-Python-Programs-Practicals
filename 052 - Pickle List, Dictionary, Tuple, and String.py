import pickle

# Data to pickle
data = {
    "list": [1, 2, 3],
    "dict": {"a": 1, "b": 2},
    "tuple": (1, 2, 3),
    "string": "Hello, World!"
}

# Pickling the data
with open("data.pkl", "wb") as file:
    pickle.dump(data, file)

# Reading the pickled data
with open("data.pkl", "rb") as file:
    loaded_data = pickle.load(file)
    print(loaded_data)
