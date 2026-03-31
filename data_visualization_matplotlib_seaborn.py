# UC9 – Apply Advanced Plot Customization Techniques

import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
days = [1, 2, 3, 4, 5]
sales = [100, 150, 130, 170, 160]
profit = [20, 30, 25, 35, 40]

# Apply seaborn style
sns.set_theme(style="darkgrid")

# Plot multiple lines
plt.plot(days, sales, marker='o', label="Sales")
plt.plot(days, profit, marker='s', label="Profit")

# Titles and labels
plt.title("Sales and Profit Trend")
plt.xlabel("Days")
plt.ylabel("Amount")

# Add legend
plt.legend()

# Add grid
plt.grid(True)

# Annotate key point
plt.annotate("Peak Sales", xy=(4, 170), xytext=(3, 180),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Show plot
plt.show()