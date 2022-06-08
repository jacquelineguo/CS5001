from friday import check_day_input, calculate_days_left
from pytest import approx


def test_check_day_input():
    assert(check_day_input("tu") == True)
    assert(check_day_input("8") == False)
    assert(check_day_input(10) == False)

def test_calculate_days_left():
    assert(calculate_days_left("tu") == 3)
    assert(calculate_days_left("sa") == 6)
    assert(calculate_days_left("su") == 5)