import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Simulating random samples from a normal distribution
sample_size = 10000
samples = np.random.normal(loc=0, scale=1, size=sample_size)

# Create a DataFrame
df = pd.DataFrame(samples, columns=["Sample"])

# Calculate the cumulative mean
df["Cumulative Mean"] = df["Sample"].expanding().mean()

# Plotting the cumulative mean
plt.plot(df["Cumulative Mean"], label="Cumulative Mean")
plt.axhline(y=0, color='r', linestyle='--', label="True Mean (0)")
plt.title("Law of Large Numbers Simulation")
plt.xlabel("Number of Samples")
plt.ylabel("Cumulative Mean")
plt.legend()
plt.show()
