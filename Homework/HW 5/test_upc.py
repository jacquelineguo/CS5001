from upc import check_item, check_calculation, is_valid_upc


def test_check_item():
    assert(not check_item("9 7 8 0 1 2 8 0 5 3 9 0 4"))
    assert(check_item("796031114977"))
    assert(not check_item("4011200296908!"))


def test_check_calculation():
    assert(not check_calculation("300819600207"))
    assert(check_calculation("300819600270"))
    assert(not check_calculation("07385400808"))


def test_is_valid_upc():
    assert(not is_valid_upc("9 7 8 0 1 2 8 0 5 3 9 0 4"))
    assert(not is_valid_upc("796031114977"))
    assert(is_valid_upc("4011200296908"))
