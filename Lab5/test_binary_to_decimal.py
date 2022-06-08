from binary_to_decimal import binary_to_decimal


def test_binary_to_decimal():
    assert(binary_to_decimal("1101") == 13)
    assert(binary_to_decimal("11010") == 26)
    assert(binary_to_decimal("100000000") == 256)