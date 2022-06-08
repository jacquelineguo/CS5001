from Factorial import calculate_factorial


def test_calculate_factorial():
    assert(calculate_factorial(6) == 720)
    assert(calculate_factorial(4) == 24)
    assert(calculate_factorial(10) == 3628800)