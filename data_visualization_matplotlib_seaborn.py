# UC8 – Generate Heatmap for Correlation Matrix

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset
data = {
    "Hours_Studied": [1, 2, 3, 4, 5],
    "Sleep_Hours": [7, 6, 6, 5, 5],
    "Practice_Tests": [1, 2, 2, 3, 4],
    "Scores": [50, 55, 65, 70, 80]
}

df = pd.DataFrame(data)

# Compute correlation matrix
correlation = df.corr()

# Apply seaborn style
sns.set_theme(style="white")

# Create heatmap
sns.heatmap(correlation, annot=True, cmap="coolwarm", linewidths=0.5)

# Title
plt.title("Feature Correlation Heatmap")

# Show plot
plt.show()