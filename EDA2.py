# STEP 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# STEP 2: Load dataset (no download needed)
df = sns.load_dataset("tips")

# STEP 3: View data
print("First 5 rows:")
print(df.head())

# STEP 4: Data information
print("\nDataset Info:")
print(df.info())

# STEP 5: Statistical summary
print("\nSummary Statistics:")
print(df.describe())

# STEP 6: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# STEP 7: Bar Plot - Total Bill by Day
sns.barplot(x='day', y='total_bill', data=df)
plt.title("Total Bill by Day")
plt.show()

# STEP 8: COLORED SCATTER PLOT (Improved 🔥)
sns.scatterplot(x='total_bill', y='tip', hue='time', data=df)
plt.title("Total Bill vs Tip")
plt.show()

# STEP 9: Regression Plot (Professional)
sns.regplot(x='total_bill', y='tip', data=df)
plt.title("Relationship Between Total Bill and Tip")
plt.show()

# STEP 10: Box Plot - Outliers
sns.boxplot(x=df['total_bill'])
plt.title("Outliers in Total Bill")
plt.show()

# STEP 11: Box Plot - Lunch vs Dinner
sns.boxplot(x='time', y='total_bill', data=df)
plt.title("Lunch vs Dinner Spending")
plt.show()

# STEP 12: Final Insights
print("\nINSIGHTS:")
print("1. Higher total bill leads to higher tips.")
print("2. Dinner time shows higher spending than lunch.")
print("3. Some outliers exist in total bill.")
print("4. Spending varies across different days.")
