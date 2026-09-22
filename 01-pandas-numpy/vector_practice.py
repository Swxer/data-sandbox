import numpy as np
import pandas as pd

df = pd.DataFrame(
    {
        "Item": ["Laptop", "Mouse", "Monitor", "Keyboard", "Desk"],
        "Price": [1200.0, 25.0, 300.0, 80.0, 450.0],
        "Quantity": [2, 15, 4, 10, 3],
    }
)

df["Total_Value"] = df["Price"] * df["Quantity"]

df["Tier"] = np.where(df["Total_Value"] > 500, "Premium", "Standard")

print(df)
