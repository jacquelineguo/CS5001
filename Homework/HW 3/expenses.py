'''
Xuan Guo
CS 5001, Fall 2020

This program gets information about the user's traveling information, then
calculates the business trip driving expenses
'''


EDGE_POINT = 0


def calculate_mileage(start, end):
    '''
        Function -- calculate_mileage
            Calculates miles driven using the start and end odometer values.
        Parameters:
            start -- The odometer reading at the start of the trip. Expecting
            a number greater than 0.
            end -- The odometer reading at the end of the trip. Expecting a
            number greater than 0 and greater than the start value.
        Returns:
            The miles driven, a number. If either parameter is invalid(e.g.
            either parameter is negative or end is less than start), returns 0.
    '''
    if start > EDGE_POINT and end > EDGE_POINT and end > start:
        return (end - start)
    else:
        return 0


def get_reimbursement_amount(mileage):
    '''
        Function -- get_reimbursement_amount
            Calculates the amount in dollars that the employee should be
            reimbursed based on their mileage and the standard rate per mile.
            The standard rate for 2020 is 57.5 cents per mile.
        Parameters:
            mileage -- The number of miles driven.
        Returns:
            The amount the employee should be reimbursed in dollars,
            a float rounded to 2 decimal places.
    '''
    MILE_TO_CENTS = 57.5
    CENTS_RATE = 100
    amount = round(mileage * MILE_TO_CENTS / CENTS_RATE, 2)
    return amount


def get_actual_mileage_rate(mpg, fuel_price):
    '''
        Function -- get_actual_mileage_rate
            Calculates the actual trip cost per mile in dollars based on the
            car's MPG and the fuel price.
        Parameters:
            mpg -- The car's miles per gallon (MPG), an integer greater than 0.
            fuel_price -- The fuel cost in dollars per gallon, a non-negative
            float.
        Returns:
            The actual cost per mile in dollars, a float rounded to 4 decimal
            places. If supplied arguments are invalid, returns 0.0
    '''
    if mpg > EDGE_POINT and fuel_price >= EDGE_POINT:
        return round(fuel_price / mpg, 4)
    else:
        return 0.0


def get_actual_trip_cost(start, end, mpg, fuel_price):
    '''
        Function -- get_actual_trip_cost
           Calculates the cost of a trip in dollars based on the miles driven,
           the MPG of the car, and the fuel price per gallon.
        Parameters:
            start -- The odometer reading at the start of the trip. Expecting a
            number greater than 0.
            end -- The odometer reading at the end of the trip. Expecting a
            number greater than 0 and greater than the start value.
            mpg -- The car's miles per gallon (MPG), an integer greater than 0.
            fuel_price -- The fuel price per gallon, a non-negative float.
        Returns:
            The cost of the drive in dollars, a float rounded to 2 decimal
            places. If any of the supplied arguments are invalid, returns 0.0
    '''
    trip_cost = calculate_mileage(start, end) * get_actual_mileage_rate(
        mpg, fuel_price)
    return round(trip_cost, 2)


def main():
    print("MILEAGE REIMBURSEMENT CALCULATOR")
    print("Options:")
    print("1 - Calculate reimbursement amount from odometer readings")
    print("2 - Calculate reimbursement amount from miles traveled")
    print("3 - Calculate the actual cost of your trip")
    choice = int(input("Enter your choice (1, 2, or 3): "))
    FIRST_CHOICE = 1
    THIRD_CHOICE = 3
    vaild_choices = [1, 2, 3]
    if choice not in vaild_choices:
        print("Not a valid choice")
    elif choice == FIRST_CHOICE or choice == THIRD_CHOICE:
        start = float(input("Enter your starting odometer reading: "))
        end = float(input("Enter your ending odometer reading: "))
        if choice == FIRST_CHOICE:
            mileage = calculate_mileage(start, end)
            rem_amount = get_reimbursement_amount(mileage)
            print("You will be reimbursed ${}".format(rem_amount))
        else:
            mpg = float(input("Enter your car's MPG: "))
            fuel_price = float(input("Enter the fuel price per gallon: "))
            trip_cost = get_actual_trip_cost(start, end, mpg, fuel_price)
            print("Your trip cost ${}".format(trip_cost))
    else:
        mileage = float(input("Enter the number of miles traveled: "))
        rem_amount = get_reimbursement_amount(mileage)
        print("You will be reimbursed ${}".format(rem_amount))


if __name__ == "__main__":
    main()
