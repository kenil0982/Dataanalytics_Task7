# Dataanalytics_Task7
# 📊 Sales Summary Analysis using SQLite and Python

This project demonstrates how to create a **basic sales analytics script** using:

- **SQLite** as the database engine (built into Python)
- **pandas** for SQL query loading and data handling
- **matplotlib** for visualizing sales data

---

## 🎯 Objective

To extract and visualize simple sales insights (total quantity sold and total revenue) from a local SQLite database (`sales_data.db`).

---

## 📁 Project Structure


---

## 🛠️ How It Works

### 1. **Database Setup**
- Connects to or creates `sales_data.db`
- Creates a `sales` table with columns: `product`, `quantity`, `price`, `region`, `date`
- Inserts sample sales data (can be customized)

### 2. **SQL Queries**
- Aggregates total quantity and total revenue **per product**
- Optionally: Aggregates total revenue **per region**

### 3. **Output**
- Prints a tabular summary using `pandas`
- Plots:
  - Bar chart of **revenue by product**
  - Pie chart of **revenue by region**
- Saves both charts as `.png` files

---

## 🖥️ How to Run

### Option 1: Using Terminal or Command Prompt
```bash
python sales_summary.py
🧩 Customization Ideas
You can extend this project further by:

Adding filters (e.g., by date, region)

Including new fields like category, salesperson

Exporting reports to Excel or CSV

Making an interactive dashboard with Plotly or Streamlit
📌 Dependencies
Python 3.x

pandas

matplotlib

sqlite3 (comes built-in with Python)
