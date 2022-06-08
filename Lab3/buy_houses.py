'''
Xuan Guo
CS 5001, Fall 2020

This program gets input from a user about their annual salary information
and house price, then calculates how long it'll take to save a down payment.
'''


MONTHS_PER_YEAR = 12

def calculate_down_payment(cost):
    '''
        Function -- calculate_down_payment
            Calculate a house's down payment
        Parameters:
            cost -- House's cost
        Returns a value of the house's down payment cost
    '''
    DOWN_PAMENT_RATE = 0.25
    down_payment = cost * DOWN_PAMENT_RATE
    return down_payment

def calculate_monthly_saving(annual_salary, saving_percent):
    '''
        Fuction -- calculate_monthly_saving
            Calculate a person's monthly saving according to his/her annual
            salary and monthly saving rate
        Parameters:
            annual_salary -- a person's annual salary
            saving_percent -- a person's monthly saving rate
        Returns a number of the person's monthly saving amount
    '''
    monthly_saving = annual_salary / MONTHS_PER_YEAR * saving_percent
    return monthly_saving

def calculate_saving_months(down_payment, monthly_saving):
    '''
        Fuction -- calculate_saving_months
            Calculate how many months needed to save the down payments=
        Parameters:
            down_payment -- house's down payment amount
            monthly_saving -- a person's monthly saving
        Returns a number of how many months needed to save down payment
    '''
    saving_months = -(-down_payment // monthly_saving)
    return saving_months

def convert_month_to_year(month):
    '''
        Fuction -- convert_month_to_year
            Conver number of months to years with months
        Parameters:
            month -- how many months to convert
        Returns a tuple of converted years and months
    '''
    years = month // MONTHS_PER_YEAR
    months = month % MONTHS_PER_YEAR
    return (years, months)

def main():
    house_cost = int(input("How much your dream house cost? "))
    annual_salary = int(input("What is your annual salary? "))
    saving_percent = float(\
        input("What percent you want to save from monthly salary? "))
    down_payment = calculate_down_payment(house_cost)
    monthly_saving = calculate_monthly_saving(annual_salary, saving_percent)
    months = calculate_saving_months(down_payment, monthly_saving)
    result = convert_month_to_year(months)
    print("Your down payment amount is: {:.2f}".format(down_payment))
    print("You can save {:.2f} per month".format(monthly_saving))
    print("Your down payment takes {:.0f} months to save".format(months))
    print(
        "Your need to save {:.0f} years, {:.0f} months"\
        .format(result[0], result[1])
        )


if __name__ == "__main__":
    main()
