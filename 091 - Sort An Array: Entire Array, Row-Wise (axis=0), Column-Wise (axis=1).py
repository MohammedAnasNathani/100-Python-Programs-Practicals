import numpy as np

# a. Entire array
arr_flat = np.array([5, 3, 8, 1, 7])
sorted_arr_flat = np.sort(arr_flat)
print("Sorted flat array:", sorted_arr_flat)
print("-" * 20)

# Example 2D array
arr_2d = np.array([[5, 2, 9], [1, 8, 3], [4, 7, 6]])
print("Original 2D array:")
print(arr_2d)
print("-" * 20)

# b. Row-wise sort (sort elements within each row independently) - axis=1
# Description: Sort each row
sorted_row = np.sort(arr_2d, axis=1)
print("Row-wise sorted array (axis=1):")
print(sorted_row)
print("-" * 20)


# c. Column-wise sort (sort elements within each column independently) - axis=0
# Description: Sort each column
sorted_column = np.sort(arr_2d, axis=0)
print("Column-wise sorted array (axis=0):")
print(sorted_column)