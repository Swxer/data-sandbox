import pandas as pd

# Sample dataset
df = pd.DataFrame(
    {
        "Category": ["Fruit", "Fruit", "Vegetable", "Vegetable", "Fruit"],
        "Product": ["Apple", "Banana", "Carrot", "Broccoli", "Orange"],
        "Price": [100.0, 50.0, 30.0, 45.0, 90.0],
        "Stock": [5, 12, 50, 30, 0],
    }
)

# Group by category and compute multiple stats cleanly
summary = (
    df.groupby("Category")
    .agg(
        Total_Stock=("Stock", "sum"),
        Average_Price=("Price", "mean"),
        Item_Count=("Product", "count"),
    )
    .reset_index()
)

another_df = pd.DataFrame(
    {
        "Department": ["Sales", "Sales", "HR", "HR", "IT"],
        "Employee": ["Alice", "Bob", "Charlie", "David", "Eve"],
        "Salary": [70000, 80000, 60000, 65000, 90000],
    }
)

another_summary = pd.DataFrame(
    another_df.groupby("Department")
    .agg(Head_Count=("Employee", "count"), Average_Salary=("Salary", "mean"))
    .reset_index()
)

print(summary)
print(another_summary)
