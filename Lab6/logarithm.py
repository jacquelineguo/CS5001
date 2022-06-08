'''
Xuan Guo
CS 5001, Fall 2020

This program gets a positive integer from user and calculates the logarithm.
'''


def log(x, base):
    '''
        Function -- log
        Parameters:
            x -- Integer which is a power of base number
            base -- Integer which is a base number
        Returns:
            The logarithm of x based to base number
    '''
    if x == 1:
        return 0
    if x == base:
        return 1
    return log(x / base, base) + 1
