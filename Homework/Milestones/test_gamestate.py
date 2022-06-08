from gamestate import GameState

# NOTE: since helper method create_board is used and only used in __init__, I\
#       will not write a seperate test case for it because it is been tested \
#       in test_gamestate_attributes
def test_gamestate_attributes():
    gs = GameState()
    assert(gs.current_player == "BLACK")
    assert(gs.selected_piece == None)
    assert(gs.moves == [])
    assert(gs.capture_moves == [])
    board = []
    for row in gs.squares:
        arr = []
        for x in row:
            if x!= "EMPTY":
                arr.append(x.color)
            else:
                arr.append("EMPTY")
        board.append(arr)
    assert(board ==
    [['EMPTY', 'BLACK', 'EMPTY', 'BLACK', 'EMPTY', 'BLACK', 'EMPTY', 'BLACK'],
    ['BLACK', 'EMPTY', 'BLACK', 'EMPTY', 'BLACK', 'EMPTY', 'BLACK', 'EMPTY'],
    ['EMPTY', 'BLACK', 'EMPTY', 'BLACK', 'EMPTY', 'BLACK', 'EMPTY', 'BLACK'], 
    ['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY'], 
    ['EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY', 'EMPTY'], 
    ['RED', 'EMPTY', 'RED', 'EMPTY', 'RED', 'EMPTY', 'RED', 'EMPTY'],
    ['EMPTY', 'RED', 'EMPTY', 'RED', 'EMPTY', 'RED', 'EMPTY', 'RED'], 
    ['RED', 'EMPTY', 'RED', 'EMPTY', 'RED', 'EMPTY', 'RED', 'EMPTY']]
        )


def test_is_my_piece():
    gs = GameState()
    assert(gs.current_player == "BLACK")
    assert(gs.squares[2][7].color == "BLACK")
    assert(gs.is_my_piece(2,7) is True)

    assert(gs.current_player == "BLACK")
    assert(gs.squares[5][4].color == "RED")
    assert(gs.is_my_piece(5,4) is False)

    assert(gs.current_player == "BLACK")
    assert(gs.squares[4][5] == "EMPTY")
    assert(gs.is_my_piece(4,5) is False)

def test_take_turn():
    gs = GameState()
    assert(gs.current_player == "BLACK")
    gs.take_turn()
    assert(gs.current_player == "RED")
    gs.take_turn()
    assert(gs.current_player == "BLACK")
