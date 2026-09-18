import pandas as pd
from sqlalchemy import create_engine


def connectToPostgres(user, password, host, port, database):
    print("Connecting to PostgreSQL...")
    # Add '+psycopg' to use the modern driver we installed
    engine = create_engine(
        f"postgresql+psycopg://{user}:{password}@{host}:{port}/{database}"
    )
    print(f"Connected to PostgreSQL: {engine}")
    return engine


engine = connectToPostgres("steven", "password123", "localhost", "5432", "sandbox_db")

new_shipment = pd.DataFrame(
    {
        "Product": ["kiwi", "papaya", "watermelon"],
        "Price": [120, 150, 200],
        "Stock": [10, 5, 8],
    }
)

print("New incoming data to add:")
print(new_shipment, "\n")

new_shipment.to_sql("inventory", con=engine, if_exists="append", index=False)

print("Success! New data appended to PostgreSQL table 'inventory'.")
