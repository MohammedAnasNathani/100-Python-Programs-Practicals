import numpy as np

# a. dtype
arr = np.array([1, 2, 3])
print("Data type:", arr.dtype)

# b. reshape
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)
print("Reshaped array:")
print(reshaped)

# c. arange
arr = np.arange(10)
print("Array using arange:", arr)

# d. empty
arr = np.empty((2, 3))
print("Empty array:")
print(arr)

# e. ones
arr = np.ones((3, 3))
print("Ones array:")
print(arr)

# f. zeros
arr = np.zeros((2, 2))
print("Zeros array:")
print(arr)

# g. asarray
list_data = [1, 2, 3]
arr = np.asarray(list_data)
print("Array from list:", arr)