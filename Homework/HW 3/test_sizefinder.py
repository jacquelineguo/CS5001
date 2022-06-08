from sizefinder import check_size_range, find_kids_size,\
    find_womens_size, find_mens_size


def test_check_size_range():
    assert(check_size_range(22))
    assert(not check_size_range(34))
    assert(check_size_range(53))


def test_find_kids_size():
    assert(find_kids_size(38) == "not available")
    assert(find_kids_size(28) == "M")
    assert(find_kids_size(33) == "XL")


def test_find_womens_size():
    assert(find_womens_size(29) == "not available")
    assert(find_womens_size(35) == "L")
    assert(find_womens_size(40) == "XXXL")


def test_find_mens_size():
    assert(find_mens_size(46) == "XXL")
    assert(find_mens_size(55) == "not available")
    assert(find_mens_size(45) == "XL")
