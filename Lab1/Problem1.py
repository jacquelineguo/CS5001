'''
Xuan Guo
CS 5001, Fall 2020

This program gets input from a user about their restaurant bill and 
calculates how much each person should pay.
'''

def main():
    bill = float(input("How much is the total amount of the bill? "))
    tip_percent = float(input("What percentage is everyone willing to tip? "))
    num_people = int(input("How many people to split the bill? "))
    total_payment = bill * (1 + tip_percent)
    per_payment = total_payment / num_people
    print("The payment for each person is: ", per_payment)

if __name__ == "__main__":
    main()