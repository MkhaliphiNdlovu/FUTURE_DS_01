# Task 1 - Business Sales Performance Analytics

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset and  read the csv file
df = pd.read_csv("sales_dataset.csv")
df.head()

# Explore dataset
df.info()
df.isnull().sum()
df = df.drop_duplicates()

# Convert date columns to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Create new calculated columns
df['Revenue'] = df['Sales']
df['Profit Margin'] = df['Profit'] / df['Sales']
df['Month_Year'] = df['Order Date'].dt.to_period('M')

# Aggregate monthly sales
monthly_sales = df.groupby('Month_Year')['Sales'].sum()

# Plot monthly sales trend
plt.figure(figsize=(12,5))
monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.xlabel("Month-Year")
plt.xticks(rotation=45)
plt.show()

# Top 10 products by sales
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_products.plot(kind='bar')
plt.title("Top 10 Products by Sales")
plt.ylabel("Sales")
plt.show()

# Sales by category
category_sales = df.groupby('Category')['Sales'].sum()

plt.figure(figsize=(6,4))
category_sales.plot(kind='bar', color='orange')
plt.title("Sales by Category")
plt.ylabel("Sales")
plt.show()

# Sales by region
region_sales = df.groupby('Region')['Sales'].sum()

plt.figure(figsize=(6,4))
region_sales.plot(kind='bar', color='green')
plt.title("Sales by Region")
plt.ylabel("Sales")
plt.show()

# Profit by category
category_profit = df.groupby('Category')['Profit'].sum()

plt.figure(figsize=(6,4))
category_profit.plot(kind='bar', color='purple')
plt.title("Profit by Category")
plt.ylabel("Profit")
plt.show()

#Top 10 products by profit
top_profit_products = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_profit_products.plot(kind='bar')
plt.title("Top 10 Profitable Products")
plt.ylabel("Profit")
plt.show()

#Sales vs Profit scater plot
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x='Sales', y='Profit')
plt.title("Sales vs Profit Relationship")
plt.show()

#print summary statistics
print("Total Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())
print("Average Profit Margin:", df['Profit Margin'].mean())

#identify top performing category and region
print("\nTop Category:", df.groupby('Category')['Sales'].sum().idxmax())
print("Top Region:", df.groupby('Region')['Sales'].sum().idxmax())

# Business insights
insights = []
insights.append("Technology products often generate high revenue and should be prioritized.")
insights.append("Certain regions outperform others, indicating better market penetration.")
insights.append("Some high sales products have low profit margins, requiring pricing review.")

#display insights
for i in insights:
    print("-", i)

