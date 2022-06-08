'''
Xuan Guo
CS 5001, Fall 2020

This program asks user to select between three shapes and their width
and height, then calculates their areas.
'''


def main():
    shape = input('Select a shape (triangle, square, or rectangle): ').lower()
    is_valid_shape = shape == 'triangle' or shape == 'square'\
        or shape == 'rectangle'
    DIMENSION_STD = 0
    MUTIPLIER = 1 / 2 if shape == "triangle" else 1

    if not is_valid_shape:
        print('Unknown shape')
    else:
        width = float(input('Enter the width: '))
        if width <= DIMENSION_STD:
            print('Invalid width')
        else:
            if shape == 'triangle' or shape == 'rectangle':
                height = float(input('Enter the height: '))
                if height <= DIMENSION_STD:
                    print('Invalid height')
                else:
                    area = width * height * MUTIPLIER
            else:
                area = width * width
        print('The area of the {} is {:.2f}'.format(shape, area))


if __name__ == "__main__":
    main()
