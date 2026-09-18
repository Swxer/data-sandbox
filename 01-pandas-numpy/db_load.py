import pandas as pd
import numpy as np
from sqlalchemy import create_engine, engine


def readCSV(file_path):
    print("Reading CSV data...")
    df = pd.read_csv(file_path, skipinitialspace=True, na_values=["", " ", "NA", "NaN"])
    df["Product"] = df["Product"].str.strip().str.lower()
    df["Price"] = pd.to_numeric(df["Price"])
    df["Stock"] = pd.to_numeric(df["Stock"])
    df = df.fillna(0)
    return df


def connectToPostgres(user, password, host, port, database):
    print("Connecting to PostgreSQL...")
    # Add '+psycopg' to use the modern driver we installed
    engine = create_engine(
        f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"
    )
    print(f"Connected to PostgreSQL: {engine}")
    return engine


df_dirty = readCSV("./01-pandas-numpy/dirty_data.csv")
print(f"Dirty DataFrame:\n{df_dirty}\n")

engine = connectToPostgres("steven", "password123", "localhost", "5432", "sandbox_db")
df_dirty.to_sql("inventory", con=engine, if_exists="replace", index=False)

print("Success! Data is now sitting safely in PostgreSQL.")
