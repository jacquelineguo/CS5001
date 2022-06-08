'''
Xuan Guo
CS5001, Fall 2020

This program represents the game state
'''
import turtle
from piece import Piece

class GameState:
    '''
        Class -- GameState
            Represent the state of the game.
        Attributes:
            squares -- A matrix representing the board containing pieces.
            current_player -- A string of current player. e.g. BLACK and RED.
            selected_piece -- A tuple of selected piece. e.g. (2,3).
            default is None.
            moves -- a list of possible next moves for current player.
            capture_moves -- a list of possible capture moves for
            current player.
            pen -- a turtle variable that does the drawing.
            screen -- a turtle module that provides turtle graphics primitives.
        Methods:
            create_board -- Helper method, create a board with pieces.
            is_my_piece -- check if current player is clicking on his piece.
            take_turn -- switch current_player's color
    '''
    def __init__(self):
        self.squares = []
        self.create_board()

        self.current_player = "BLACK"
        self.selected_piece = None
        self.moves = []
        self.capture_moves = []

        self.pen = turtle.Turtle() # This variable does the drawing.
        self.pen.hideturtle() # This gets rid of the triangle cursor.
        self.screen = turtle.Screen()


    def create_board(self):
        '''
            Method -- create_board
                Create a board with pieces arranged in initial setting.
            Parameter:
                self -- the current GameState object
            Returns:
                returns nothing
        '''
        TWO = 2
        LOWER = 3
        UPPER = 5
        NUM_SQUARES = 8
        for i in range(NUM_SQUARES):
            row = []
            for j in range(NUM_SQUARES):
                color = ''
                directions = []
                if j % TWO != i % TWO and i < LOWER:
                    color = 'BLACK'
                    directions.append([1, -1])
                    directions.append([1, 1])
                elif j % TWO != i % TWO and i >= UPPER:
                    color = 'RED'
                    directions.append([-1, 1])
                    directions.append([-1, -1])
                else:
                    row.append("EMPTY")
                    continue
                piece = Piece(color, directions)
                row.append(piece)
            self.squares.append(row)


    def is_my_piece(self, x, y):
        '''
            Method -- create_board
                check if current player is clicking on his piece.
            Parameters:
                self -- the current GameState object
                x -- the x coordinate of the click
                y -- the y coordinate of the click
            Returns:
                returns true if current player clicked their piece,
                false otherwise
        '''
        if not self.squares or not self.squares[0]:
            print("ERROR, board is empty")
        elif self.squares[x][y] != "EMPTY":
            return self.current_player == self.squares[x][y].color
        return False


    def take_turn(self):
        '''
            Method -- create_board
                switch color between RED and BLACK for current_player attribute
            Parameters:
                self -- the current GameState object
            Returns:
                returns nothing
        '''
        self.current_player = \
            "BLACK" if self.current_player == "RED" else "RED"
