import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [25000, 30000, 35000, 40000, 45000, 50000]

plt.bar(months, sales)
plt.xlabel('Months')
plt.ylabel('Sales')
plt.title('Sales Trend over Last 6 Months')
plt.show()
