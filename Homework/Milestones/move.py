'''
Xuan Guo
CS5001, Fall 2020

This program represents a move
'''
class Move:
    '''
        Class -- Move
            Represent the move of a piece
        Attributes:
            start -- a tuple representing the start coordinates
            end -- a tuple representing the end coordinates
            is_capture -- a boolean value showing whether it is a capture move
    '''
    def __init__(self, start, end, is_capture):
        self.start = start
        self.end = end
        self.is_capture = is_capture
