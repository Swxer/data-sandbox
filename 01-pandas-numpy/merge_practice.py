import pandas as pd

# Table 1: Employees and their Department IDs
employees = pd.DataFrame(
    {
        "Emp_ID": [1, 2, 3, 4],
        "Name": ["Alice", "Bob", "Charlie", "Diana"],
        "Dept_ID": [10, 20, 10, 30],
    }
)

# Table 2: Department IDs and Department Names
departments = pd.DataFrame(
    {"Dept_ID": [10, 20, 40], "Dept_Name": ["Engineering", "Marketing", "Finance"]}
)

# Merge them together using a Left Join on 'Dept_ID'
merged_df = pd.merge(employees, departments, on="Dept_ID", how="left")


customers = pd.DataFrame(
    {"CustomerID": [1, 2, 3, 4], "CustomerName": ["Johnny", "Steve", "Zack", "Kim"]}
)

orders = pd.DataFrame(
    {
        "OrderId": [1111, 2222, 3333, 4444],
        "CustomerID": [1, 2, 3, 4],
        "OrderAmount": [50, 70, 20, 100],
    }
)

merged_df_2 = pd.merge(customers, orders, on="CustomerID", how="left")


print(merged_df_2)
