
# Project Documentation

## Main Goal

This project implements a basic Extract, Transform, Load (ETL) pipeline. The goal is to read data from CSV files, transform it into a dimensional model, and load it into a SQLite data warehouse. This allows for easier and more efficient data analysis.

## File Descriptions

### `customers.csv`

This file contains customer data, including their ID, name, and region.

- `customer_id`: Unique identifier for each customer.
- `name`: Name of the customer.
- `region`: Region where the customer is located.

### `orders.csv`

This file contains order data.

- `order_id`: Unique identifier for each order.
- `customer_id`: Foreign key referencing `customers.csv`.
- `product_id`: Foreign key referencing `products.csv`.
- `order_date`: Date the order was placed.
- `quantity`: Quantity of the product ordered.

### `products.csv`

This file contains product data.

- `product_id`: Unique identifier for each product.
- `product_name`: Name of the product.
- `category`: Category the product belongs to.
- `price`: Price of the product.

### `sql-load.py`

This Python script performs the ETL process:

1.  **Extract**: Reads the data from `customers.csv`, `orders.csv`, and `products.csv`.
2.  **Transform**:
    - Merges the orders and products data.
    - Calculates the revenue for each order.
    - Creates a time dimension from the order dates.
3.  **Load**:
    - Connects to a SQLite database named `warehouse.db`.
    - Loads the transformed data into four tables:
        - `Customers_Dim`: Customer dimension table.
        - `Products_Dim`: Product dimension table.
        - `Time_Dim`: Time dimension table.
        - `Sales_Fact`: Fact table containing sales data.

### `queries.py`

This script demonstrates how to query the data warehouse. It connects to `warehouse.db` and executes a SQL query to calculate the total revenue by product category.

### `warehouse.db`

This is the SQLite database file created by `sql-load.py`. It contains the data warehouse with the dimension and fact tables.

### `README.md`

The main documentation of the project.
