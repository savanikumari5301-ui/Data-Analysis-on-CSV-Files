import os
import matplotlib.pyplot as plt
import pandas as pd

# --- STEP 1: CREATE A SAMPLE CSV FILE (To ensure the code runs immediately) ---
sample_data = {
    "Region": [
        "North",
        "South",
        "East",
        "West",
        "North",
        "South",
        "East",
        "West",
        "North",
        "South",
    ],
    "Product": [
        "Laptop",
        "Mobile",
        "Laptop",
        "Tablet",
        "Mobile",
        "Laptop",
        "Tablet",
        "Laptop",
        "Tablet",
        "Mobile",
    ],
    "Sales": [12000, 8000, 15000, 5000, 9000, 11000, 6000, 13000, 4500, 8500],
    "Quantity": [15, 20, 18, 10, 22, 14, 12, 16, 9, 21],
}

df_sample = pd.DataFrame(sample_data)
df_sample.to_csv("sales_data.csv", index=False)
print("✅ Success: 'sales_data.csv' created locally.")

# --- STEP 2: LOAD CSV USING PANDAS ---
# Reads the CSV file into a pandas DataFrame
df = pd.read_csv("sales_data.csv")

# --- STEP 3: DATA EXPLORATION (.head() and .shape) ---
print("\n--- First 5 Rows of the Dataset ---")
print(df.head())

print(f"\nDataFrame Shape (Rows, Columns): {df.shape}")

# --- STEP 4: DATA ANALYSIS (groupby() and sum()) ---
# Group by 'Product' and calculate total sales for each
product_sales = df.groupby("Product")["Sales"].sum().reset_index()
print("\n--- Total Sales by Product ---")
print(product_sales)

# --- STEP 5: VISUALIZATION (plot()) ---
# Creating a bar chart for sales performance
plt.figure(figsize=(8, 5))
plt.bar(
    product_sales["Product"], product_sales["Sales"], color="skyblue", edgecolor="black"
)
plt.title("Total Sales Value by Product", fontsize=14, fontweight="bold")
plt.xlabel("Product Category", fontsize=12)
plt.ylabel("Total Sales ($)", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Display the chart
plt.tight_layout()
plt.show()