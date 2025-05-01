import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# --------------------------
# 1. Connect to SQLite Database
# --------------------------
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# --------------------------
# 2. Create Sales Table (only once)
# --------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    region TEXT,
    date TEXT
)
""")

# --------------------------
# 3. Insert Sample Data (customizable!)
# --------------------------
sample_data = [
    # product, quantity, price, region, date
    ('Apple', 10, 2.5, 'North', '2025-04-01'),
    ('Banana', 20, 1.0, 'South', '2025-04-02'),
    ('Orange', 15, 1.5, 'West', '2025-04-03'),
    ('Mango', 12, 3.0, 'East', '2025-04-01'),
    ('Grapes', 18, 2.2, 'North', '2025-04-04'),
    ('Watermelon', 6, 4.5, 'South', '2025-04-05'),
    ('Pineapple', 9, 3.5, 'East', '2025-04-06'),
    ('Apple', 7, 2.5, 'West', '2025-04-07'),
    ('Mango', 9, 3.0, 'North', '2025-04-02'),
    ('Banana', 30, 1.0, 'West', '2025-04-08'),
    ('Orange', 8, 1.5, 'East', '2025-04-09'),
    ('Watermelon', 4, 4.5, 'South', '2025-04-10'),
    ('Pineapple', 6, 3.5, 'North', '2025-04-11'),
    ('Grapes', 14, 2.2, 'East', '2025-04-12'),
    ('Apple', 20, 2.5, 'South', '2025-04-13'),
]

cursor.executemany("INSERT INTO sales (product, quantity, price, region, date) VALUES (?, ?, ?, ?, ?)", sample_data)
conn.commit()

# --------------------------
# 4. Query: Total Quantity and Revenue per Product
# --------------------------
query = """
SELECT product,
       SUM(quantity) AS total_quantity,
       ROUND(SUM(quantity * price), 2) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC
"""
df_summary = pd.read_sql_query(query, conn)
print("\n🔹 Total Quantity and Revenue per Product:\n")
print(df_summary)

# --------------------------
# 5. Optional: Region-wise Summary
# --------------------------
region_query = """
SELECT region,
       ROUND(SUM(quantity * price), 2) AS region_revenue
FROM sales
GROUP BY region
ORDER BY region_revenue DESC
"""
df_region = pd.read_sql_query(region_query, conn)
print("\n🔹 Revenue by Region:\n")
print(df_region)

# --------------------------
# 6. Plot: Revenue per Product
# --------------------------
plt.figure(figsize=(10, 5))
df_summary.plot(kind='bar', x='product', y='total_revenue', color='orange', legend=False)
plt.title("💰 Revenue by Product")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("revenue_by_product.png")
plt.show()

# --------------------------
# 7. Plot: Revenue by Region
# --------------------------
df_region.plot(kind='pie', y='region_revenue', labels=df_region['region'], autopct='%1.1f%%', legend=False)
plt.title("📍 Revenue Distribution by Region")
plt.ylabel("")
plt.tight_layout()
plt.savefig("revenue_by_region.png")
plt.show()

# --------------------------
# 8. Close the Connection
# --------------------------
conn.close()
