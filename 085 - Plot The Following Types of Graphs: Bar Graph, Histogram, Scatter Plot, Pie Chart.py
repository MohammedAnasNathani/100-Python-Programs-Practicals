# a. Bar Graph
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [4, 7, 2, 9]

plt.bar(categories, values)
plt.title('Bar Graph')
plt.show()

# b. Histogram
import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)
plt.hist(data, bins=30, edgecolor='black')
plt.title('Histogram')
plt.show()

# c. Scatter Plot
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.scatter(x, y)
plt.title('Scatter Plot')
plt.show()

# d. Pie Chart
import matplotlib.pyplot as plt

labels = ['Apple', 'Banana', 'Cherry', 'Date']
sizes = [15, 30, 45, 10]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()
