import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
new_column = np.array([[7], [8]])

arr_with_new_column = np.hstack([arr, new_column])
print("Array after adding new column:")
print(arr_with_new_column)
