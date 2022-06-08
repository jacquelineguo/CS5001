from expenses import calculate_mileage, get_reimbursement_amount,\
    get_actual_mileage_rate, get_actual_trip_cost
from pytest import approx


def test_calculate_mileage():
    assert(calculate_mileage(600, 1500) == 900)
    assert(calculate_mileage(0, -1) == 0)
    assert(calculate_mileage(1000, 6000) == 5000)


def test_get_reimbursement_amount():
    assert(get_reimbursement_amount(1000) == 575.00)
    assert(get_reimbursement_amount(565) == 324.88)
    assert(get_reimbursement_amount(888.4) == 510.83)


def test_get_actual_mileage_rate():
    assert(get_actual_mileage_rate(24, 2.99) == 0.1246)
    assert(get_actual_mileage_rate(18, 3.99) == 0.2217)
    assert(get_actual_mileage_rate(0, -5) == 0.0)


def test_get_actual_trip_cost():
    assert(get_actual_trip_cost(1000, 1010, 36, 3.09) == 0.86)
    approx(get_actual_trip_cost(566, 800, 18, 3.65) == 47.45)
    approx(get_actual_trip_cost(6000, 6500, 27, 3.29) == 60.93)
