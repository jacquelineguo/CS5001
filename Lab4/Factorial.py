'''
Xuan Guo
CS 5001, Fall 2020

This program asks user to enter an integer and calculates it's factorial
'''


def calculate_factorial(num):
    '''
        Function -- calculate_factorial
        Parameter:
            num -- An positive integer
        Return the factorial of num
    '''
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result


def main():
    # Ask user to input an integer
    num = int(input("Enter an integer: "))
    # Calculate the factorial
    factorial = calculate_factorial(num)
    print("The factorial of number {} is {}".format(num, factorial))


if __name__ == "__main__":
    main()