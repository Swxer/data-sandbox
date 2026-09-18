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

query = 'SELECT "Product", "Price", "Stock" FROM inventory WHERE "Price" > 80;'

df_result = pd.read_sql_query(query, con=engine)

print("Query Results from PostgreSQL:")
print(df_result)
