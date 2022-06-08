'''
Xuan Guo
CS 5001, Fall 2020

This program gets a positive integer from user and calculates the logarithm 
base 2.
'''


def calculate_log(x, base):
    '''
        Function -- calculate_log
        Parameters:
            x -- Integer which is a power of base number
            base -- Integer which is a base number
        Return the logarithm of x based to base number
    '''
    STOP_POINT = 1
    times = 0
    while (x / base) >= STOP_POINT:
        times += 1
        x = x / base
    return times


def main():
    # Ask user to enter a positive integer
    num = int(input("Enter a positive power of 2: "))
    BASE = 2
    # Calculate the logarithm of user entered number based to 2
    result = calculate_log(num, BASE)
    print("lg ({}) = {}".format(num, result))


if __name__ == "__main__":
    main()
