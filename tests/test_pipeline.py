def test_income():
    income = 25000 + 85000 + 45000 + 65000 + 65000
    assert income == 285000


def test_expenses():
    expenses = 5000 + 4500 + 12000 - 5000
    assert expenses == 16500


def test_balance():
    income = 285000
    expenses = 16500

    assert income - expenses == 268500