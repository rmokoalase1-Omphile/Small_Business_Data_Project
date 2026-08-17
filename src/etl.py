import pandas as pd
import sqlite3


def calculate_total(quantity, unit_price):
    return quantity * unit_price


def validate_quantity(quantity):
    return quantity > 0


def run_etl():

    # 1. Read the raw sales data
    df = pd.read_csv("data/raw/sales.csv")

    print("Raw data:")
    print(df)

    # 2. Clean the data
    df["date"] = pd.to_datetime(df["date"])

    df["quantity"] = pd.to_numeric(
        df["quantity"],
        errors="coerce"
    )

    df["unit_price"] = pd.to_numeric(
        df["unit_price"],
        errors="coerce"
    )

    # 3. Calculate total sales
    df["total_sale"] = df["quantity"] * df["unit_price"]

    # 4. Remove incomplete records
    df = df.dropna()

    # 5. Save cleaned data
    df.to_csv(
        "data/processed/cleaned_sales.csv",
        index=False
    )

    # 6. Create SQLite database
    connection = sqlite3.connect("database/sales.db")

    df.to_sql(
        "sales",
        connection,
        if_exists="replace",
        index=False
    )

    connection.close()

    print("\nETL pipeline completed successfully!")
    print(f"Records processed: {len(df)}")
    print(f"Total revenue: R{df['total_sale'].sum():,.2f}")


if __name__ == "__main__":
    run_etl()