'''
Xuan Guo
CS 5001, Fall 2020

This program gets the number and operation inputs from users, then running the
calculation as the user asked
'''


def calculation(num):
    '''
        Function -- calculation
        Parameter:
            num -- user entered number
        Returns the result of user's asked operation of the number
    '''
    i = 0
    result = num
    while i != 1:
        operator = input("Enter the next step in the calculation: ")
        if operator == "q" or operator == "Q":
            i = 1
            word_output = "Total"
        else:
            if operator[0] == "+":
                result = result + float(operator[1:])
            elif operator[0] == "-":
                result = result - float(operator[1:])
            elif operator[0] == "*":
                result = result * float(operator[1:])
            else:
                result = result / float(operator[1:])
            print("Subtotal = {}".format(result))
            i = 0
    return (word_output, result)

def main():
    # Ask user to input a number
    num = float(input("Enter a number: "))
    result = calculation(num)
    print("{} = {}".format(result[0], result[1]))
    

if __name__ == "__main__":
    main()
