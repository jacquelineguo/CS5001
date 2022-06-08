'''
Xuan Guo
CS 5001, Fall 2020

This programs returns the greatest common divisor of two or non-zero positive
integers
'''


def GCD(num1, num2):
    '''
        Function -- GCD
            Calculates the greatest common divisor of two non-zero positive
            integers
        Parameters:
            num1 -- first integer
            num2 -- second integer
        Returns:
            The greatest common divisor of two non-zero positive integers
    '''
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    if num1 > num2:
        return GCD(num2, num1 % num2)
    return GCD(num1, num2 % num1)


def GCD_nums(lst):
    '''
        Function -- GCD_nums
            Calculates the greatest common divisor of more than two non-zero
            positive integers
        Parameters:
            lst -- a list contains non-zero positive integers
        Returns:
            The greatest common divisor of the integers in the list
    '''
    if len(lst) == 2:
        return GCD(lst[0], lst[1])
    return GCD(lst[0], GCD_nums(lst[1:]))
