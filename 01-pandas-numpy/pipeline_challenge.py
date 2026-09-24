import numpy as np
import pandas as pd

# Raw transaction data
transactions = pd.DataFrame(
    {
        "OrderID": [101, 102, 103, 104, 105],
        "CustomerID": [1, 2, 1, 3, 2],
        "CustomerName": [
            "  john doe",
            "JANE SMITH ",
            "  john doe  ",
            "bob builder",
            "JANE SMITH ",
        ],
        "OrderDateStr": [
            "2026-01-10 10:00:00",
            "2026-02-15 14:30:00",
            "2026-03-20 09:15:00",
            "2026-04-05 16:45:00",
            "2026-05-12 11:00:00",
        ],
        "Price": [150.0, 45.0, 200.0, 80.0, 300.0],
        "Quantity": [2, 4, 1, 5, 2],
    }
)

# Region lookup data
regions = pd.DataFrame(
    {
        "CustomerID": [1, 2, 3],
        "Region": ["North", "South", "East"],
    }
)


def clean_text(df):
    df["CleanName"] = df["CustomerName"].str.strip().str.title()
    return df


def parse_date(df):
    df["OrderDateStr"] = pd.to_datetime(df["OrderDateStr"])
    df["OrderMonth"] = df["OrderDateStr"].dt.month
    return df


def calculate_total(df):
    df["TotalAmount"] = df["Price"] * df["Quantity"]
    return df


def determineHighValue(df):
    df["HighValueOrder"] = np.where(df["TotalAmount"] > 200, "Yes", "No")
    return df


def merge_data(df1, df2):
    return pd.merge(df1, df2, on="CustomerID", how="left")


def aggregate(df):
    return (
        df.groupby("Region")
        .agg(
            TotalRevenue=("TotalAmount", "sum"),
            TotalOrders=("OrderID", "count"),
            AvgPrice=("Price", "mean"),
        )
        .reset_index()
    )


def display(df):
    print(df)


transactions = clean_text(transactions)
transactions = parse_date(transactions)
transactions = calculate_total(transactions)
transactions = determineHighValue(transactions)
transactions = merge_data(transactions, regions)
region_data = aggregate(transactions)
display(transactions)
display(region_data)
