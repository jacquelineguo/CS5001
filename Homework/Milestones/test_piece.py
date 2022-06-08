from piece import Piece


def test_piece_attributes():
    p = Piece("RED", [[1, -1], [1, 1]])
    assert(p.color == "RED")
    assert(p.directions == [[1, -1], [1, 1]])
    assert(p.king is False)


def test_add_directions():
    p = Piece("RED", [[1, -1], [1, 1]])
    assert(p.directions == [[1, -1], [1, 1]])
    p.add_directions([[-1, 1], [-1, -1]])
    assert(p.directions == [[1, -1], [1, 1], [-1, 1], [-1, -1]])


def test_coronation():
    p = Piece("BLACK", [[1, -1], [1, 1]])
    assert(p.directions == [[1, -1], [1, 1]])
    assert(p.king is False)
    p.coronation()
    assert(p.directions == [[1, -1], [1, 1], [-1, 1], [-1, -1]])
    assert(p.king is True)
