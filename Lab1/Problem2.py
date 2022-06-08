'''
Xuan Guo
CS 5001, Fall 2020

This program gets input from a user about their annual salary information
and house price, then calculates how long it'll take to save a down payment.
'''

def main():
    house_cost = int(input("How much your dream house cost? "))
    annual_salary = int(input("What is your annual salary? "))
    saving_percent = float(input("What percent you want to save from monthly salary? "))
    down_payment_rate = 0.25
    down_payment = house_cost * down_payment_rate
    months_per_year = 12
    monthly_saving = annual_salary / months_per_year * saving_percent
    saving_months = -(-down_payment // monthly_saving)
    years = saving_months // months_per_year
    months = saving_months % months_per_year
    print("Your down payment amount is:", down_payment)
    print("You can save", monthly_saving, "per month")
    print("Your down payment takes", saving_months, "months to save")
    print("Your need to save", years, "years,", months, "months")

if __name__ == "__main__":
    main()