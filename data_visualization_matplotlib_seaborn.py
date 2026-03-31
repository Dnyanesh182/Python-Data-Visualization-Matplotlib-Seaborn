# UC6 – Visualize Proportions using Pie Chart

import matplotlib.pyplot as plt

# Sample data (e.g., market share)
labels = ["Product A", "Product B", "Product C", "Product D"]
sizes = [40, 25, 20, 15]

# Optional explode to highlight a segment
explode = (0.1, 0, 0, 0)

# Create pie chart
plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, startangle=90)

# Equal aspect ratio ensures circle
plt.axis('equal')

# Title
plt.title("Market Share Distribution")

# Show plot
plt.show()