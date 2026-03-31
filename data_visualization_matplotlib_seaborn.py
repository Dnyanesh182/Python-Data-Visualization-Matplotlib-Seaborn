# UC10 – Perform End-to-End EDA using Visualizations

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataset (can be replaced with CSV load)
data = {
    "Day": [1, 2, 3, 4, 5],
    "Sales": [100, 150, 130, 170, 160],
    "Profit": [20, 30, 25, 35, 40],
    "Category": ["A", "B", "A", "B", "A"]
}

df = pd.DataFrame(data)

# Basic inspection
print(df.head())
print(df.describe())

# Apply seaborn theme
sns.set_theme(style="whitegrid")

# 🔹 Line Plot (Trend)
plt.figure()
plt.plot(df["Day"], df["Sales"], marker='o')
plt.title("Sales Trend")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()

# 🔹 Bar Chart (Category Comparison)
plt.figure()
sns.barplot(x="Category", y="Sales", data=df)
plt.title("Sales by Category")
plt.show()

# 🔹 Histogram (Distribution)
plt.figure()
sns.histplot(df["Sales"], bins=5, kde=True)
plt.title("Sales Distribution")
plt.show()

# 🔹 Pie Chart (Proportion)
plt.figure()
df["Category"].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Category Distribution")
plt.ylabel("")
plt.show()

# 🔹 Scatter Plot (Correlation)
plt.figure()
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

# 🔹 Heatmap (Correlation Matrix)
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()