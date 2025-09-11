import pandas as pd
import sqlite3

# --- Step 1. Extract ---
orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")

# --- Step 2. Transform ---
# Join orders with products to calculate revenue
orders = orders.merge(products, on="product_id")
orders["revenue"] = orders["quantity"] * orders["price"]

# --- Step 3. Load ---
# Connect to SQLite database (creates file if it doesn't exist)
conn = sqlite3.connect("warehouse.db")

# Save dimension tables
customers.to_sql("Customers_Dim", conn, if_exists="replace", index=False)
products.to_sql("Products_Dim", conn, if_exists="replace", index=False)

# Create Time_Dim
time_dim = pd.DataFrame()
time_dim["date"] = pd.to_datetime(orders["order_date"].unique())
time_dim["month"] = time_dim["date"].dt.month
time_dim["year"] = time_dim["date"].dt.year
time_dim.to_sql("Time_Dim", conn, if_exists="replace", index=False)

# Save fact table
sales_fact = orders[["order_id", "customer_id", "product_id", "quantity", "revenue", "order_date"]]
sales_fact.to_sql("Sales_Fact", conn, if_exists="replace", index=False)

conn.close()

print("✅ ETL complete! Data loaded into warehouse.db")
