from buy_houses import calculate_down_payment, calculate_monthly_saving, calculate_saving_months, convert_month_to_year
from pytest import approx

def test_calculate_down_payment():
    assert(calculate_down_payment(700000) == 175000.00)
    assert(calculate_down_payment(1000000) == 250000.00)
    assert(calculate_down_payment(50000) == 12500.00)

def test_calculate_monthly_saving():
    approx(calculate_monthly_saving(80000, 0.5) == 3333.33)
    approx(calculate_monthly_saving(50000, 0.4) == 1666.67)
    assert(calculate_monthly_saving(60000, 0.3) == 1500.00)

def test_calculate_saving_months():
    assert(calculate_saving_months(250000, 5000) == 50)
    approx(calculate_monthly_saving(100000, 6000) == 17)
    approx(calculate_monthly_saving(270000, 7000) == 39)

def test_convert_month_to_year():
    assert(convert_month_to_year(50) == (4, 2))
    assert(convert_month_to_year(60) == (5, 0))
    assert(convert_month_to_year(71) == (5, 11))