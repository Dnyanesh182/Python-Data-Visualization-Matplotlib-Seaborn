# UC7 – Develop Scatter Plot for Correlation Analysis

import matplotlib.pyplot as plt
import seaborn as sns

# Sample data (e.g., hours studied vs exam scores)
hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [35, 40, 50, 55, 65, 70, 75, 85]

# Apply seaborn style
sns.set_theme(style="whitegrid")

# Create scatter plot
plt.scatter(hours, scores)

# Labels and title
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Scores")

# Grid for readability
plt.grid(True)

# Show plot
plt.show()