'''
Xuan Guo
CS5001, Fall 2020

This program asks user to enter a binary number and converts it to decimal
number
'''


def binary_to_decimal(binary):
    '''
        Function -- binary_to_decimal
        Parameters:
            binary -- a string contains a binary number
        Returns:
            A transformed decimal number according to the inputted 
            binary number
    '''
    if len(binary) == 1 and binary[0] == "1":
        return 1
    if len(binary) == 1 and binary[0] == "0":
        return 0
    return 2 ** (len(binary) - 1) * int(binary[0]) +\
        binary_to_decimal(binary[1:])
