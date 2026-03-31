# UC5 – Analyze Data Distribution using Histogram

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Generate sample numerical data (e.g., exam scores)
data = np.random.normal(loc=70, scale=10, size=100)

# Apply seaborn style
sns.set_theme(style="whitegrid")

# Create histogram with KDE (density curve)
sns.histplot(data, bins=10, kde=True, color='blue')

# Labels and title
plt.title("Distribution of Scores")
plt.xlabel("Scores")
plt.ylabel("Frequency")

# Show plot
plt.show()