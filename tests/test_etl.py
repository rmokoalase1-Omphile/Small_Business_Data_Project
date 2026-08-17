from src.etl import calculate_total, validate_quantity


def test_revenue_calculation():
    total = calculate_total(2, 50)

    assert total == 100


def test_large_order():
    total = calculate_total(10, 25)

    assert total == 250


def test_single_item():
    total = calculate_total(1, 75)

    assert total == 75


def test_quantity_must_be_positive():
    assert validate_quantity(5) is True


def test_negative_quantity_is_invalid():
    assert validate_quantity(-5) is False