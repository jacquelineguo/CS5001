from GCD import GCD, GCD_nums


def test_GCD():
    assert(GCD(270, 192) == 6)
    assert(GCD(54, 24) == 6)
    assert(GCD(5236, 9850) == 2)


def test_GCD_nums():
    assert(GCD_nums([56, 89, 6]) == 1)
    assert(GCD_nums([600, 56, 86]) == 2)
    assert(GCD_nums([666, 36, 72]) == 18)