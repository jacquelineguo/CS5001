'''
Xuan Guo
CS5001, Fall 2020

This program helps user to draw stars
'''
import turtle


def draw_star(a_turtle, length, size, space):
    '''
        Function -- draw_star
        Parameters:
            a_turtle -- an instance of Turtle
            length -- the length of the line
            size -- the number of stars to draw
            space -- the length to next star
        Returns:
            Nothing. Draws the star as asked
    '''
    COLORS = ['red', 'yellow', 'green', 'blue', 'orange']
    ANGLE = 144
    a_turtle.pendown()
    n = 0
    while n < size:
        for i in range(5):
            a_turtle.color(COLORS[i])
            a_turtle.forward(length)
            a_turtle.right(ANGLE)
            length += space
        n += 1
    a_turtle.penup()


def draw_star_recursion(a_turtle, length, size, space):
    '''
        Function -- draw_star
        Parameters:
            a_turtle -- an instance of Turtle
            length -- the length of the line
            size -- the number of stars to draw
            space -- the length to next star
        Returns:
            Nothing. Draws the star as asked
    '''
    COLORS = ['red', 'yellow', 'green', 'blue', 'orange']
    ANGLE = 144
    a_turtle.pendown()
    if size > 1:
        for i in range(5):
            a_turtle.color(COLORS[i])
            a_turtle.forward(length)
            a_turtle.right(ANGLE)
            length += space
        draw_star_recursion(a_turtle, length, size-1, space)


def main():
    pen = turtle.Turtle()
    draw_star_recursion(pen, 10, 6, 15)
    turtle.done()

if __name__ == "__main__":
    main()
