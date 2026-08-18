import pandas as pd

from src.analysis import best_selling_products, regular_customers


def test_best_selling_products():
    data = pd.DataFrame({
        "product": ["Rice", "Bread", "Rice", "Milk"],
        "quantity": [3, 2, 1, 2]
    })

    result = best_selling_products(data)

    assert result.iloc[0]["product"] == "Rice"


def test_regular_customers():
    data = pd.DataFrame({
        "customer_id": ["C001", "C001", "C002", "C002", "C002"],
        "customer_name": [
            "Thabo Mokoena",
            "Thabo Mokoena",
            "Amanda Smith",
            "Amanda Smith",
            "Amanda Smith"
        ]
    })

    result = regular_customers(data)

    assert result.iloc[0]["customer_name"] == "Amanda Smith"
    assert result.iloc[0]["number_of_purchases"] == 3