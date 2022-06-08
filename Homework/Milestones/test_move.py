from move import Move


def test_move_attributes():
    m = Move((2, 7), (3, 6), False)
    assert(m.start == (2, 7))
    assert(m.end == (3, 6))
    assert(m.is_capture is False)
