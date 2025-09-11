import sqlite3
import pandas as pd

conn = sqlite3.connect("warehouse.db")

query = """
SELECT p.category, SUM(f.revenue) AS total_revenue
FROM Sales_Fact f
JOIN Products_Dim p ON f.product_id = p.product_id
GROUP BY p.category;
"""

df = pd.read_sql_query(query, conn)
print(df)

conn.close()
