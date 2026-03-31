# UC2 – Implement Line Graph for Trend Analysis

import matplotlib.pyplot as plt

# Sample time-series data (e.g., days vs sales)
days = [1, 2, 3, 4, 5]
sales = [100, 150, 130, 170, 160]

# Create line plot
plt.plot(days, sales, marker='o', linestyle='-', linewidth=2)

# Labels and title
plt.title("Sales Trend Over Time")
plt.xlabel("Days")
plt.ylabel("Sales")

# Grid for better readability
plt.grid(True)

# Display plot
plt.show()