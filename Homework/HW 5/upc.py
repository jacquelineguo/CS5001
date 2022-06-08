'''
Xuan Guo
CS5001, Fall 2020

This program help user to check if the inputted Universal Product Code is valid
'''


ZEROS = 0


def check_item(upc):
    '''
        Function -- check_item
            Check if the inputted parameters only contain numbers
        Parameters:
            upc -- A Universal Product Code which is a series of string
        Returns:
            True is only contain numbers, False if not
    '''
    VALID_ITEM = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for item in upc:
        if item not in VALID_ITEM:
            return False
    return True


def check_calculation(upc):
    '''
        Function -- check_calculation
            Check if the sum of even position and odd position mutiply by 3 can
            be divide by 10.
        Parameters:
            upc -- A Universal Product Code which is a series of string
        Returns:
            True if the total can be divided by 10, False if not
    '''
    total = 0
    IS_EVEN = 2
    MUTIPLIER = 3
    DIVIDENT = 10
    converted_upc = upc[::-1]
    for index, value in enumerate(converted_upc):
        if index % IS_EVEN == ZEROS:
            total += int(value)
        else:
            total += (int(value) * MUTIPLIER)
    return total % DIVIDENT == ZEROS


def is_valid_upc(upc):
    '''
        Function -- is_valid_upc
            Check if the input parameter is a valid Universal Product Code
        Parameters:
            upc -- A Universal Product Code which is a series of string
        Returns:
            True if the input is not empty, not contain other characters other
            than numbers, and the sum of even position and odd position mutiply
            by 3 can be divide by 10, False if one of the three condition false
    '''
    return len(upc) != ZEROS and check_item(upc) and check_calculation(upc)
