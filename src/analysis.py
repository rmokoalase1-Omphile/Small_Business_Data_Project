import pandas as pd


def best_selling_products(df):
    result = (
        df.groupby("product")["quantity"]
        .sum()
        .reset_index()
    )

    result = result.rename(
        columns={"quantity": "units_sold"}
    )

    return result.sort_values(
        "units_sold",
        ascending=False
    ).reset_index(drop=True)