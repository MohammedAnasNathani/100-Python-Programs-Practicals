import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
new_row = np.array([[7, 8, 9]])

arr_with_new_row = np.vstack([arr, new_row])
print("Array after adding new row:")
print(arr_with_new_row)
