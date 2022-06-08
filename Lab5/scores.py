'''
Xuan Guo
CS5001, Fall 2020

This program computes statistics for a class of students' scores
'''


ZERO = 0


def average(grades):
    '''
        Function -- average
        Parameters:
            grades -- a list contains students' grade
        Returns:
            The average grade of a class
    '''
    if len(grades) == ZERO:
        return ZERO
    else:
        total = 0
        for grade in grades:
            total += grade
        return total / len(grades)


def median(grades):
    '''
        Function -- median
        Parameters:
            grades -- a list contains students' grade
        Returns:
            The median grade of a class
    '''
    sorted_grades = sorted(grades)
    length = len(grades)
    HALF = 2
    INDEX_DIFF = 1
    if length == ZERO:
        return 0
    if length % HALF == ZERO:
        median = (sorted_grades[int(length / HALF)] +
        sorted_grades[int(length / HALF - INDEX_DIFF)]) / HALF
    else:
        median = sorted_grades[length // HALF]
    return median


def lowest(grades):
    '''
        Function -- lowest
        Parameters:
            grades -- a list contains students' grade
        Returns:
            The lowest grade of the class grades
    '''
    if len(grades) == 0:
        return 0
    sorted_grades = sorted(grades)
    return sorted_grades[0]


def highest(grades):
    '''
        Functions -- highest
        Parameters:
            grades -- a list contains students' grade
        Returns:
            The highest grade of the class grades
    '''
    if len(grades) == 0:
        return 0
    sorted_grades = sorted(grades)
    return sorted_grades[-1]


def main():
    i = 0
    grades = []
    while i != 1:
        num = int(input("Enter the grade of a student (-1 to quit): "))
        if num < 0:
            i = 1
        else:
            grades.append(num)
    EMPTY = 0
    if len(grades) != EMPTY:
        ave = average(grades)
        med = median(grades)
        low = lowest(grades)
        high = highest(grades)
        print("The average of the class grades is: {}".format(ave))
        print("The median of the class grades is: {}".format(med))
        print("The lowest grade in class is: {}".format(low))
        print("The highest grade in class is: {}".format(high))


if __name__ == "__main__":
    main()
