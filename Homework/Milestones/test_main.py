from main import on_board, check_possible_moves, bot, \
    human, move, capture, GameState


def test_on_board():
    assert(on_board(0, 1) == True)
    assert(on_board(175, 25) == False)
    assert(on_board(-23, -20) == False)
    assert(on_board(-147, 219) == False)
    assert(on_board(0, 0) == False)


def test_check_possible_moves():
    gameState = GameState()
    mvs, cmvs = check_possible_moves(5,4,gameState)
    assert(len(mvs) == 2)
    assert(mvs[0].start == (5,4))
    assert(mvs[0].end == (4,5))
    assert(mvs[0].is_capture == False)
    assert(mvs[1].start == (5,4))
    assert(mvs[1].end == (4,3))
    assert(mvs[1].is_capture == False)
    assert(cmvs == [])

    mvs, cmvs = check_possible_moves(0,3,gameState)
    assert(mvs == [])
    assert(cmvs == [])


def test_bot():
    gameState = GameState()
    gameState.take_turn()
    assert(gameState.current_player == "RED")
    assert(len(gameState.moves) == 0)
    bot(gameState)
    assert(gameState.current_player == "BLACK")
    assert(len(gameState.moves) > 0)


def test_human():
    gameState = GameState()
    # first test if clicked on invalid area
    assert(gameState.current_player == "BLACK")
    assert(gameState.selected_piece == None)
    assert(len(gameState.moves) == 0)
    human(0, 0, gameState)
    assert(gameState.current_player == "BLACK")
    assert(gameState.selected_piece == None)
    assert(len(gameState.moves) == 0)

    # test the first click to select a piece to move
    gameState = GameState()
    assert(gameState.current_player == "BLACK")
    assert(gameState.selected_piece == None)
    assert(len(gameState.moves) == 0)
    human(2, 7, gameState)
    assert(gameState.current_player == "BLACK")
    assert(gameState.selected_piece == (2,7))
    assert(len(gameState.moves) > 0)

    # test the second click to move a piece
    assert(gameState.current_player == "BLACK")
    assert(gameState.selected_piece == (2, 7))
    assert(len(gameState.moves) > 0)
    human(3, 6, gameState)
    assert(gameState.current_player == "RED")
    assert(gameState.selected_piece == None)
    assert(len(gameState.moves) > 0)


def test_move():
    gameState = GameState()
    assert(gameState.squares[2][7].color == "BLACK")
    assert(gameState.squares[2][7].directions == [[1, -1], [1, 1]])
    assert(gameState.squares[2][7].king == False)
    assert(gameState.squares[3][6] == "EMPTY")
    move(2, 7, 3, 6, gameState)
    assert(gameState.squares[2][7] == "EMPTY")
    assert(gameState.squares[3][6].color == "BLACK")
    assert(gameState.squares[3][6].directions == [[1, -1], [1, 1]])
    assert(gameState.squares[3][6].king == False)


def test_capture():
    gameState = GameState()
    # set up capture conditions
    move(2, 7, 3, 6, gameState)
    gameState.take_turn()
    move(5, 4, 4, 5, gameState)
    gameState.take_turn()

    assert(gameState.squares[3][6].color == "BLACK")
    assert(gameState.squares[3][6].directions == [[1, -1], [1, 1]])
    assert(gameState.squares[3][6].king == False)
    assert(gameState.squares[4][5].color == "RED")
    assert(gameState.squares[4][5].directions == [[-1, 1], [-1, -1]])
    assert(gameState.squares[4][5].king == False)
    assert(gameState.squares[5][4] == "EMPTY")
    capture(3, 6, 5, 4, gameState)
    assert(gameState.squares[3][6] == "EMPTY")
    assert(gameState.squares[4][5] == "EMPTY")
    assert(gameState.squares[5][4].color == "BLACK")
    assert(gameState.squares[5][4].directions == [[1, -1], [1, 1]])
    assert(gameState.squares[5][4].king == False)
