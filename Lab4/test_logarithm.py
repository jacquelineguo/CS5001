from Logarithm import calculate_log


def test_calculate_log():
    assert(calculate_log(64, 2) == 6)
    assert(calculate_log(125, 5) == 3)
    assert(calculate_log(46656, 6) == 6)