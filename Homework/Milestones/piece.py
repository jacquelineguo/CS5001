'''
Xuan Guo
CS5001, Fall 2020

This program represents a piece of checker
'''
class Piece:
    '''
        Class -- Piece
            Represent a piece of checker
        Attributes:
            color -- a string representing color of the piece
            directions -- a list of lists indicating directions a piece can go
            king -- a boolean value representing whether a piece is the king
        Methods:
            add_directions -- add new possible directions for the piece
            coronation -- make the piece a king piece
    '''
    def __init__(self, color, directions):
        self.color = color
        self.directions = directions
        self.king = False


    def add_directions(self, new_directions):
        '''
            Method -- add_directions
                Add new directions in the direction list
            Parameters:
                self -- the current Piece object
                new_directions -- a list of new directions
            Return:
                Nothing. Add new directions in the direction list
        '''
        self.directions += new_directions


    def coronation(self):
        '''
            Method -- coronation
                Make the piece a king and add backward directions for it.
            Parameters:
                self -- the current Piece object
            Return:
                returns nothing.
        '''
        new_dir = [[-1, 1], [-1, -1]] if \
            self.color == "BLACK" else [[1, -1], [1, 1]]
        self.add_directions(new_dir)
        self.king = True
