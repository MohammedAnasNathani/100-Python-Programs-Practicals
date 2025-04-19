import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Max element in the entire array:", np.max(arr))
print("Index of max element:", np.unravel_index(np.argmax(arr), arr.shape))

print("Max elements of each column:", np.max(arr, axis=0))
print("Max elements of each row:", np.max(arr, axis=1))
