# UC4 – Design Bar Chart for Categorical Comparison

import matplotlib.pyplot as plt
import seaborn as sns

# Sample categorical data
categories = ["Product A", "Product B", "Product C", "Product D"]
sales = [120, 150, 90, 180]

# Apply seaborn style
sns.set_theme(style="whitegrid")

# Create bar chart
plt.bar(categories, sales, color=['blue', 'green', 'orange', 'red'])

# Labels and title
plt.title("Product Sales Comparison")
plt.xlabel("Products")
plt.ylabel("Sales")

# Rotate labels for readability (if needed)
plt.xticks(rotation=30)

# Show plot
plt.show()