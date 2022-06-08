from logarithm import log


def test_log():
    assert(log(64, 2) == 6)
    assert(log(125, 5) == 3)
    assert(log(46656, 6) == 6)
