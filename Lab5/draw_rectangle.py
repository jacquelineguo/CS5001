'''
Xuan Guo
CS5001, Fall 2020

This program asks user to enter a rectangle's width, height, and a symbal to
express. Then print out the rectangle.
'''


def draw_rectangle(width, height, char):
    '''
        Function -- draw_rectangle
        Parameters:
            width -- the width of a rectangle
            heigth -- the heigth of a rectangle
            char -- the symbal to draw the rectangle
        Returns:
            A rectangle shape string
    '''
    FIRST_ROW = 0
    LAST_ROW = height - 1
    result1 = ""
    result = ""
    DIFF = 2
    for i in range(height):
        result1 = ""
        if i == FIRST_ROW or i == LAST_ROW:
            for a in range(width):
                result1 += char 
        else:
            result1 = "\n" + char + " " * (width - DIFF) + char + "\n"
        result = result + result1
    return result

def main():
    width = int(input("Enter the width of your rectangle: "))
    height = int(input("Enter the height of your rectangle: "))
    char = input("Enter a character to draw your rectangle: ")
    print(draw_rectangle(width, height, char))


if __name__ == "__main__":
    main()
