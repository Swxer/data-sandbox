import pandas as pd

# Data with date strings
# df = pd.DataFrame(
#     {
#         "Order_ID": [101, 102, 103],
#         "Order_Date_Str": ["2026-01-15", "2026-05-20", "2026-09-01"],
#     }
# )

# # 1. Convert string to actual datetime objects
# df["Order_Date"] = pd.to_datetime(df["Order_Date_Str"])

# # 2. Extract specific parts using the .dt accessor
# df["Year"] = df["Order_Date"].dt.year
# df["Month"] = df["Order_Date"].dt.month
# df["DayName"] = df["Order_Date"].dt.day_name()

# print(df[["Order_Date", "Year", "Month", "DayName"]])

df = pd.DataFrame(
    {
        "Event": ["Signup", "Subscription", "Renewal"],
        "Timestamp": [
            "2026-03-10 14:30:00",
            "2026-04-12 09:15:00",
            "2026-05-01 18:45:00",
        ],
    }
)

df["Timestamp"] = pd.to_datetime(df["Timestamp"])
df["Event_Month"] = df["Timestamp"].dt.month
df["Event_Hour"] = df["Timestamp"].dt.hour

print(df)
