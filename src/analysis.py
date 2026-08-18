import pandas as pd


def best_selling_products(data):
    return (
        data.groupby("product", as_index=False)["quantity"]
        .sum()
        .sort_values(
            by=["quantity", "product"],
            ascending=[False, True]
        )
        .reset_index(drop=True)
    )

def regular_customers(data):
    return (
        data.groupby(["customer_id", "customer_name"])
        .size()
        .sort_values(ascending=False)
        .reset_index(name="number_of_purchases")
    )