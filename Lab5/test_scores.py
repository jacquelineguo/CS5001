from scores import average, median, lowest, highest
from pytest import approx


grade1 = [1, 2, 3, 4, 5, 6]
grade2 = [85, 60, 90, 75, 99, 98, 100, 71, 97]
grade3 = []


def test_average():
    assert(average(grade1) == 3.5)
    approx(average(grade2) == 86.111)
    assert(average(grade3) == 0)


def test_median():
    assert(median(grade1) == 3.5)
    assert(median(grade2) == 90)
    assert(median(grade3) == 0)


def test_lowest():
    assert(lowest(grade1) == 1)
    assert(lowest(grade2) == 60)
    assert(lowest(grade3) == 0)


def test_highest():
    assert(highest(grade1) == 6)
    assert(highest(grade2) == 100)
    assert(highest(grade3) == 0)