import pandas as pd

# A messy dataset with weird spacing, mixed cases, and typos
# df = pd.DataFrame(
#     {
#         "Raw_Email": ["  ALICE@gmail.com ", "BOB@Yahoo.COM", "Charlie@gmail.com  "],
#         "Product_Code": ["item-101", " ITEM-102 ", "item-103"],
#     }
# )

# # Clean up strings using the .str accessor
# df["Clean_Email"] = df["Raw_Email"].str.strip().str.lower()
# df["Clean_Code"] = df["Product_Code"].str.strip().str.upper()

# print(df[["Clean_Email", "Clean_Code"]])


df = pd.DataFrame(
    {
        "Customer_Name": ["  john doe", "JANE SMITH ", "  bob johnson  "],
        "City": ["new york", "LOS ANGELES", "chicago "],
    }
)


df["Clean_Name"] = df["Customer_Name"].str.strip().str.title()
df["Clean_City"] = df["City"].str.strip().str.upper()

print(df[["Clean_Name", "Clean_City"]])
