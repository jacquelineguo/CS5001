'''
Xuan Guo
CS 5001, Fall 2020

This code is a milestone project for further steps of checker game program
'''
import turtle
import random
from gamestate import GameState
from move import Move
from piece import Piece


NUM_SQUARES = 8 # The number of squares on each row.
SQUARE = 50 # The size of each square in the checkerboard.
SQUARE_COLORS = ("light gray", "black")
CHECKER_COLOR = {1: "black", 2: "red"}
TWO = 2
OFFSET = 4
ZERO = 0
SEVEN = 7
CENTER_Y = -45
gameState = GameState()


def on_board(i, j):
    '''
        Function -- on_board
            Check whether a click is on the board
        Parameters:
            i -- x coordinate of the click
            j -- y coordinate of the click
        Returns:
            return True if click is on the board, false otherwise.
    '''
    return ZERO <= i < NUM_SQUARES and ZERO <= j < NUM_SQUARES and \
        i % TWO != j % TWO


def check_possible_moves(i, j, gameState=gameState, piece=None):
    '''
        Function -- check_possible_moves
            Check possible next moves
        Parameters:
            i -- x coordinate of the piece being moved
            j -- y coordinate of the piece being moved
            gameState -- the current GameState object
            pieve -- the piece being moved, optional, default is None
        Returns:
            return lists of possible moves and capture moves
    '''
    if not piece:
        piece = gameState.squares[i][j]
    moves, capture_moves = [], []
    if piece != "EMPTY":
        directions = piece.directions
        for dir in directions:
            move_row = i + dir[0]
            move_col = j + dir[1]
            if on_board(move_row, move_col):
                if gameState.squares[move_row][move_col] == "EMPTY":
                    move = Move((i, j), (move_row, move_col), False)
                    moves.append(move)
                elif gameState.squares[move_row][move_col].color != \
                    gameState.current_player:
                    leap_row = move_row + dir[0]
                    leap_col = move_col + dir[1]
                    if on_board(leap_row, leap_col) and \
                        gameState.squares[leap_row][leap_col] == "EMPTY":
                        move = Move((i, j), (leap_row, leap_col), True)
                        capture_moves.append(move)
    return moves, capture_moves


def click_handler(x, y):
    '''
        Function -- click_handler
            Called when a click occurs.
        Parameters:
            x -- X coordinate of the click. Automatically provided by Turtle.
            y -- Y coordinate of the click. Automatically provided by Turtle.
        Returns:
            Does not and should not return. Click handlers are a special type
            of function automatically called by Turtle. You will not have
            access to anything returned by this function.
    '''
    i = int(y // SQUARE) + OFFSET
    j = int(x // SQUARE) + OFFSET
    if gameState.current_player == "BLACK":
        human(i, j)
    if gameState.current_player == "RED":
        gameState.screen.ontimer(bot, 1000)


def bot(gameState=gameState):
    '''
        Function -- bot
            Process computer players moves in a random manner
        Parameters:
            gameState -- the current GameState object
        Returns:
            return nothing.
    '''
    for ii in range(NUM_SQUARES):
        for jj in range(NUM_SQUARES):
            if gameState.squares[ii][jj] != "EMPTY" and \
                gameState.squares[ii][jj].color == gameState.current_player:
                moves, capture_moves = check_possible_moves(ii, jj)
                gameState.moves += moves
                gameState.capture_moves += capture_moves

    # check if player wins
    if not gameState.moves and not gameState.capture_moves:
        print("win")
        gameState.pen.goto(ZERO, CENTER_Y)
        gameState.pen.pencolor("green")
        gameState.pen.write(
            "GAME OVER!\n\n", align="CENTER", font=("Verdana", 40, "normal")
            )
        gameState.pen.write(
            "You Win!", align="CENTER", font=("Verdana", 40, "normal")
            )
        return

    if gameState.capture_moves:
        mv = random.choice(gameState.capture_moves)
        capture(mv.start[0], mv.start[1], mv.end[0], mv.end[1])
    else:
        mv = random.choice(gameState.moves)
        move(mv.start[0], mv.start[1], mv.end[0], mv.end[1])

    # reset possible next moves
    gameState.moves = []
    gameState.capture_moves = []
    gameState.take_turn()
    for ii in range(NUM_SQUARES):
        for jj in range(NUM_SQUARES):
            if gameState.squares[ii][jj] != "EMPTY" and \
                gameState.squares[ii][jj].color == gameState.current_player:
                moves, capture_moves = check_possible_moves(ii, jj)
                gameState.moves += moves
                gameState.capture_moves += capture_moves

    # check if play loses
    if not gameState.moves and not gameState.capture_moves:
        print("lose")
        gameState.pen.goto(ZERO, CENTER_Y)
        gameState.pen.pencolor("green")
        gameState.pen.write(
            "GAME OVER!\n\n", align="CENTER", font=("Verdana", 40, "normal")
            )
        gameState.pen.write(
            "You lost", align="CENTER", font=("Verdana", 40, "normal")
            )
        return


def human(i, j, gameState=gameState):
    '''
        Function -- human
            Process human players moves.
        Parameters:
            i -- x coordinate of the click position
            j -- y coordinate of the click position
            gameState -- the current GameState object
        Returns:
            return nothing.
    '''
    if gameState.selected_piece:
        success = False
        if gameState.capture_moves:
            for mv in gameState.capture_moves:
                _, capture_moves = check_possible_moves(mv.end[0], mv.end[1], \
                    gameState, gameState.squares[mv.start[0]][mv.start[1]])
                if mv.end == (i, j) and mv.start == gameState.selected_piece:
                    success = capture(gameState.selected_piece[0], \
                        gameState.selected_piece[1], i, j)
                    break

                if capture_moves:
                    finished = False
                    for leap_mv in capture_moves:
                        if leap_mv.end == (i, j) and mv.start == \
                            gameState.selected_piece:
                            success = capture(mv.start[0], mv.start[1], \
                                mv.end[0], mv.end[1])
                            success = capture(mv.end[0], mv.end[1], i, j)
                            finished = True
                            break
                    if finished:
                        break
        else:
            for mv in gameState.moves:
                if mv.end == (i, j) and mv.start == gameState.selected_piece:
                    success = move(gameState.selected_piece[0], \
                        gameState.selected_piece[1], i, j)
                    break
        lights_out()
        gameState.selected_piece = None
        if success:
            gameState.moves = []
            gameState.capture_moves = []
            gameState.take_turn()
            for ii in range(NUM_SQUARES):
                for jj in range(NUM_SQUARES):
                    if gameState.squares[ii][jj] != "EMPTY" and \
                        gameState.squares[ii][jj].color == \
                            gameState.current_player:
                        moves, capture_moves = check_possible_moves(ii, jj)
                        gameState.moves += moves
                        gameState.capture_moves += capture_moves
    else:
        if not gameState.is_my_piece(i, j):
            print("please select correct piece")
        else:
            gameState.selected_piece = (i, j)
            for ii in range(NUM_SQUARES):
                for jj in range(NUM_SQUARES):
                    if gameState.squares[ii][jj] != "EMPTY" and \
                        gameState.squares[ii][jj].color == \
                            gameState.current_player:
                        moves, capture_moves = check_possible_moves(ii, jj)
                        gameState.moves += moves
                        gameState.capture_moves += capture_moves
            light_up()


def light_up():
    '''
        Function -- light_up
            turn square color blue on selected piece and red on possible
            next move. Will show blue color on piece if a capture is possible.
        Parameters:
            None
        Returns:
            return nothing.
    '''
    if gameState.capture_moves:
        for cm in gameState.capture_moves:
            gameState.pen.setposition((cm.start[1] - OFFSET) * SQUARE, \
                (cm.start[0] - OFFSET) * SQUARE)
            draw_square(gameState.pen, SQUARE, "blue")
            # possible next move
            gameState.pen.setposition((cm.end[1] - OFFSET) * SQUARE, \
                (cm.end[0] - OFFSET) * SQUARE)
            draw_square(gameState.pen, SQUARE, "red")
        return
    for m in gameState.moves:
        if m.start == gameState.selected_piece:
            gameState.pen.setposition((m.start[1] - OFFSET) * SQUARE, \
                (m.start[0] - OFFSET) * SQUARE)
            draw_square(gameState.pen, SQUARE, "blue")
            # possible next move
            gameState.pen.setposition((m.end[1] - OFFSET) * SQUARE, \
                (m.end[0] - OFFSET) * SQUARE)
            draw_square(gameState.pen, SQUARE, "red")


def lights_out():
    '''
        Function -- lights_out
            remove any border color on the board
        Parameters:
            None
        Returns:
            return nothing.
    '''
    if gameState.capture_moves:
        for cm in gameState.capture_moves:
            gameState.pen.setposition((cm.start[1] - OFFSET) * SQUARE, \
                (cm.start[0] - OFFSET) * SQUARE)
            draw_square(gameState.pen, SQUARE, "black")
            gameState.pen.setposition((cm.end[1] - OFFSET) * SQUARE, \
                (cm.end[0] - OFFSET) * SQUARE)
            draw_square(gameState.pen, SQUARE, "black")
        return
    for m in gameState.moves:
        if m.start == gameState.selected_piece:
            gameState.pen.setposition((m.start[1] - OFFSET) * SQUARE, \
                (m.start[0] - OFFSET) * SQUARE)
            draw_square(gameState.pen, SQUARE, "black")
            gameState.pen.setposition((m.end[1] - OFFSET) * SQUARE, \
                (m.end[0] - OFFSET) * SQUARE)
            draw_square(gameState.pen, SQUARE, "black")


def move(i, j, x, y, gameState=gameState):
    '''
        Function -- move
            move a piece from (i, j) to (x, y)
        Parameters:
            i -- x coordinate of the checker's original position will be moved
            j -- y coordinate of the checker's original position will be moved
            x -- x coordinate of the checker's next position
            y -- y coordinate of the checker's next position
            gameState -- the current GameState object
        Returns:
            True if it is a succesful move
    '''
    HALF_S = SQUARE / TWO
    remove_checker((j - OFFSET) * SQUARE, (i - OFFSET) * SQUARE)
    piece = gameState.squares[i][j]
    if piece == "EMPTY":
        print("ERROR, no piece to be moved")
        return False
    gameState.squares[i][j] = "EMPTY"
    if x == ZERO or x == SEVEN:
        piece.coronation()
    if piece.king:
        draw_king(gameState.current_player, \
                (y - OFFSET) * SQUARE + HALF_S, (x - OFFSET) * SQUARE)
    else:
        draw_checker(gameState.current_player, \
                (y - OFFSET) * SQUARE + HALF_S, (x - OFFSET) * SQUARE)
    gameState.squares[x][y] = piece
    return True


def capture(i, j, x, y, gameState=gameState):
    '''
        Function -- capture
            move a piece from (i, j) to (x, y), capturing the piece in middle
        Parameters:
            i -- x coordinate of the checker's original position will be moved
            j -- y coordinate of the checker's original position will be moved
            x -- x coordinate of the checker's next position
            y -- y coordinate of the checker's next position
            gameState -- the current GameState object
        Returns:
            True if it is a succesful capture
    '''
    HALF_S = SQUARE / TWO
    middle_x, middle_y = i + (x - i) // TWO, j + (y - j) // TWO

    remove_checker((j - OFFSET) * SQUARE, (i - OFFSET) * SQUARE)
    piece = gameState.squares[i][j]
    if piece == "EMPTY":
        print("ERROR, no piece to be moved")
        return False
    gameState.squares[i][j] = "EMPTY"

    remove_checker((middle_y - OFFSET) * SQUARE, \
        (middle_x - OFFSET) * SQUARE)
    gameState.squares[middle_x][middle_y] = "EMPTY"
    if x == ZERO or x == SEVEN:
        piece.coronation()
    if piece.king:
        draw_king(gameState.current_player, \
                (y - OFFSET) * SQUARE + HALF_S, (x - OFFSET) * SQUARE)
    else:
        draw_checker(gameState.current_player, \
                (y - OFFSET) * SQUARE + HALF_S, (x - OFFSET) * SQUARE)
    gameState.squares[x][y] = piece
    return True


def draw_square(a_turtle, size, color = None):
    '''
        Function -- draw_square
        Parameters:
            a_turtle -- an instance of turtle
            size -- the length of the square
        Returns:
            Nothing. Draw a square.
    '''
    RIGHT_ANGLE = 90
    FOUR = 4
    a_turtle.pendown()
    if color:
        a_turtle.pencolor(color)
    for i in range(FOUR):
        a_turtle.forward(size)
        a_turtle.left(RIGHT_ANGLE)
    a_turtle.penup()


def draw_board(a_turtle, num, coner):
    '''
        Function -- draw_board
        Parameters:
            a_turtle -- an instance of turtle
            num -- the number of squares on each row
            coner -- the coordinate of the left side bottom coner
        Returns:
            Nothing. Draw the board of the game
    '''
    a_turtle.color(SQUARE_COLORS[1], SQUARE_COLORS[0])
    for col in range(num):
        for row in range(num):
            if row % TWO != col % TWO:
                a_turtle.begin_fill()
            a_turtle.setposition(coner + row * SQUARE, coner + col * SQUARE)
            draw_square(a_turtle, SQUARE)
            a_turtle.end_fill()


def draw_checker(color, x, y):
    '''
        Function -- draw_checker
            Draw a circle with radius.
        Parameters:
            color -- the checker color
            x -- x coordinate of a start point
            y -- y coordinate of a start point
        Returns:
            Nothing. Draws a circle as a checker in the graphics square.
    '''
    a_turtle = gameState.pen
    a_turtle.setposition(x, y)
    a_turtle.color(color)
    a_turtle.begin_fill()
    a_turtle.pendown()
    a_turtle.circle(SQUARE / TWO)
    a_turtle.penup()
    a_turtle.end_fill()


def draw_king(color, x, y):
    '''
        Function -- draw_king
            Draw a circle with letter K in it.
        Parameters:
            color -- the checker color
            x -- x coordinate of a start point
            y -- y coordinate of a start point
        Returns:
            Nothing. Draws a circle with letter K as a king checker
            in the graphics square.
    '''
    a_turtle = gameState.pen
    a_turtle.setposition(x, y)
    a_turtle.color(color)
    a_turtle.begin_fill()
    a_turtle.pendown()
    a_turtle.circle(SQUARE / TWO)
    a_turtle.pencolor("grey")
    a_turtle.write("K", align="CENTER", font=("Verdana", 45, "normal"))
    a_turtle.penup()
    a_turtle.end_fill()


def draw_checkers(a_turtle, num, coner):
    '''
        Function -- draw_checkers
        Parameters:
            a_turtle -- an instance of turtle
            num -- the number of checkers on each row
            coner -- the coordinate of the left side bottom coner
        Returns:
            Nothing. Draw the checkers with different colors of the game
    '''
    PLAYER_POS = [0, 1, 2]
    COMPUTER_POS = [5, 6, 7]
    CHECKER_COLOR = ""
    for col in range(num):
        for row in range(num):
            if  row % TWO != col % TWO and col in PLAYER_POS:
                CHECKER_COLOR = "black"
            elif row % TWO != col % TWO and col in COMPUTER_POS:
                CHECKER_COLOR = "red"
            else:
                continue
            X = coner + SQUARE/TWO + row * SQUARE
            Y = coner + col * SQUARE
            draw_checker(CHECKER_COLOR, X, Y)


def remove_checker(x, y):
    '''
        Function -- remove_checker
        Parameters:
            x -- x coordinate of removing point
            y -- y coordinate of removing point
        Returns:
            Nothing, draw a empty grey square
    '''
    a_turtle = gameState.pen
    a_turtle.setposition(x, y)
    a_turtle.color(SQUARE_COLORS[1], SQUARE_COLORS[0])
    a_turtle.begin_fill()
    draw_square(a_turtle, SQUARE)
    a_turtle.end_fill()


def main():
    board_size = NUM_SQUARES * SQUARE
    # Create the UI window. 
    window_size = board_size + SQUARE # The extra + SQUARE is the margin
    turtle.setup(window_size, window_size)
    turtle.screensize(board_size, board_size)
    turtle.bgcolor("white") # The window's background color
    turtle.tracer(0, 0) # makes the drawing appear immediately
    gameState.pen.penup() # This allows the pen to be moved.
    gameState.pen.color("black", "white")
    # Draw a square as the board line of checkerboard
    coner = -board_size / TWO
    gameState.pen.setposition(coner, coner)
    draw_square(gameState.pen, board_size)

    # Draw the colored checkerboard
    draw_board(gameState.pen, NUM_SQUARES, coner)

    # Draw checkers
    draw_checkers(gameState.pen, NUM_SQUARES, coner)

    # Click handling
    gameState.screen.onclick(click_handler)

    turtle.done() # Stops the window from closing.


if __name__ == "__main__":
    main()
