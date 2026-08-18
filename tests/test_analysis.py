import pandas as pd

from src.analysis import best_selling_products


def test_best_selling_products():
    data = pd.DataFrame({
        "product": ["Rice", "Bread", "Rice", "Milk"],
        "quantity": [2, 3, 2, 2]
    })

    result = best_selling_products(data)

    assert result.iloc[0]["product"] == "Rice"
    assert result.iloc[0]["units_sold"] == 4