'''
Xuan Guo
CS 5001, Fall 2020

This program gets information about the user's chest measurement and return
the correct T-shirt size to the user
'''


def check_size_range(chest_size):
    '''
        Function -- check_size_range
        Parameters:
            chest_size -- user's chest measurement in inches
        Returns:
            Retures True if the chest measurement is not in the size chart of
            kids', women's, and men's
    '''
    LOWER_BOUND = 26
    UPPER_BOUND = 52
    if chest_size < LOWER_BOUND or chest_size >= UPPER_BOUND:
        return True
    else:
        return False


OUT_OF_RANGE = "not available"
INCHESE_TO_SIZE = {0: "S", 1: "M", 2: "L", 3: "XL", 4: "XXL", 5: "XXXL"}


def find_kids_size(chest_size):
    '''
        Function -- find_kids_size
        Parameter:
            chest_size -- user's chest measurement in inches
        Returns:
            The size of kids'
    '''
    INCHES_TO_SIZE_KIDS = {0: "S", 1: "M", 2: "L", 3: "XL", 4: "XXL"}
    OFFSET = 2
    LOWER_BOUND = 26
    UPPER_BOUND = 36
    if chest_size < LOWER_BOUND or chest_size >= UPPER_BOUND:
        kid_size = OUT_OF_RANGE
    else:
        kid_size = INCHES_TO_SIZE_KIDS[(chest_size - LOWER_BOUND) // OFFSET]
    return kid_size


def find_womens_size(chest_size):
    '''
        Function -- find_womens_size
        Parameter:
            chest_size -- user's chest measurement in inches
        Returns:
            The size of women's
    '''
    LOWER_BOUND = 30
    UPPER_BOUND = 42
    OFFSET = 2
    if chest_size < LOWER_BOUND or chest_size >= UPPER_BOUND:
        women_size = OUT_OF_RANGE
    else:
        women_size = INCHESE_TO_SIZE[(chest_size - LOWER_BOUND) // OFFSET]
    return women_size


def find_mens_size(chest_size):
    '''
        Function -- find_mens_size
        Parameter:
            chest_size -- user's chest measurement in inches
        Returns:
            The size of men's
    '''
    LOWER_BOUND = 34
    UPPER_BOUND = 52
    OFFSET = 3
    if chest_size < LOWER_BOUND or chest_size >= UPPER_BOUND:
        men_size = OUT_OF_RANGE
    else:
        men_size = INCHESE_TO_SIZE[(chest_size - LOWER_BOUND) // OFFSET]
    return men_size


def main():
    chest_size = float(input("Chest measurement in inches: "))
    if check_size_range(chest_size):
        print("Sorry, we don't carry your size")
    else:
        print("Your size choices:")
        kid_size = find_kids_size(chest_size)
        women_size = find_womens_size(chest_size)
        men_size = find_mens_size(chest_size)
        print("Kids size: " + kid_size)
        print("Womens size: " + women_size)
        print("Mens size: " + men_size)


if __name__ == "__main__":
    main()
