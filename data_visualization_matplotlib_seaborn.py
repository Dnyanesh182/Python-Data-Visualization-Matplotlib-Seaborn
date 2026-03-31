# UC3 – Build Enhanced Line Plot with Seaborn Styling

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset
data = pd.DataFrame({
    "Day": [1, 2, 3, 4, 5],
    "Sales": [100, 150, 130, 170, 160]
})

# Apply seaborn theme
sns.set_theme(style="darkgrid")

# Create enhanced line plot
sns.lineplot(data=data, x="Day", y="Sales", marker='o', color='b')

# Labels and title
plt.title("Sales Trend Analysis (Seaborn Styled)")
plt.xlabel("Day")
plt.ylabel("Sales")

# Show plot
plt.show()