# UC1 – Initialize Data Visualization Environment

import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

# Basic plot
plt.plot(x, y)

# Add title and labels
plt.title("Basic Line Plot - Setup Validation")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Show plot
plt.show()