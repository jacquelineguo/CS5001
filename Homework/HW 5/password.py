'''
Xuan Guo
CS5001, Fall 2020

This program takes a string as password and check if it is a secure passwaord
'''


def count_char(password):
    '''
        Function -- count_char
            This function count the different character types in a string
        Parameters:
            password -- a series of string
        Returns:
            The count inforamtion of different data types in the string
            includes four special characters, numbers, lowercase letters,
            uppercase letters, and other than those four.
    '''
    SPECIAL_CHAR = ["$", "#", "@", "!"]
    count_special = 0
    count_lower = 0
    count_upper = 0
    count_num = 0
    count_others = 0
    for i in password:
        if i.isdigit():
            count_num += 1
        elif i in SPECIAL_CHAR:
            count_special += 1
        elif i.islower():
            count_lower += 1
        elif i.isupper():
            count_upper += 1
        else:
            count_others += 1
    return count_special, count_num, count_lower, count_upper, count_others


def secure_password(password):
    '''
        Function -- secure_password
            This function check if a password is a secure password
        Parameters:
            password -- a series of string
        Returns:
            True if the length of the string is between 9 and 12 (inclusive),
            and contains at least one lowercase letters, uppercase letters,
            numbers, and one of four special characters. False if not.
    '''
    length = len(password)
    PW_STD = 0
    SMALLEST_LEN = 9
    LARGEST_LEN = 12
    CONDITIONS = 3
    if length >= SMALLEST_LEN and length <= LARGEST_LEN:
        count_special, count_num, count_lower, count_upper, count_others =\
            count_char(password)
        if count_others == PW_STD:
            is_valid_pw = (count_num > PW_STD) + (count_lower > PW_STD) +\
                (count_upper > PW_STD) + (count_special > PW_STD)
            if is_valid_pw >= CONDITIONS:
                return True
    return False
