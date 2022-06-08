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
    BASE = 2
    last_index = len(binary) - 1
    result = 0
    for index, value in enumerate(binary):
        result += BASE ** (last_index - index) * int(value)
    return result


def main():
    bin_num = input("Enter a binary number: ")
    dec_num = binary_to_decimal(bin_num)
    print("Converted decimal number is: {}".format(dec_num))


if __name__ == "__main__":
    main()
