'''
Xuan Guo
CS 5001, Fall 2020

This program gets input from a user about their annual salary information
and house price, then calculates how long it'll take to save a down payment.
'''


def check_day_input(day):
    '''
        Fuction -- check_day_input
            Check if the user enter a correct weekday
        Parameters:
            day -- user's input of a day
        Returns True if day entered is from 
        ["m", "tu", "w", "th", "f", "sa", "su"], and False if not.
    '''
    vaild_day = ["m", "tu", "w", "th", "f", "sa", "su"]
    if day in vaild_day:
        return True
    else:
        return False

def calculate_days_left(current_day):
    '''
        Fuction -- calculate_days_left
            Calculates how many days left until Friday
        Parameters:
            current_day -- Today's day from user's input
        Returns days left until Friday
    '''
    weekdays = {"m": 1, "tu": 2, "w": 3, "th": 4, "f": 5, "sa": 6, "su": 7}
    WEEKDAYS = 7
    for key, value in weekdays.items():
        if key == current_day and value < weekdays["f"]:
            days_left = weekdays["f"] - value
        elif key == current_day and value >= weekdays["f"]:
            days_left = (weekdays["f"] - value) % WEEKDAYS
    return days_left
        

def main():
    user_name = input("Enter your name: ")
    print("Hello, ", user_name)
    current_day = input("Enter the current day: ").lower()
    if not check_day_input(current_day):
        print("Not a correct day to enter!")
    else:
        days_left = calculate_days_left(current_day)
        print("There are {} days until Friday!".format(days_left))


if __name__ == "__main__":
    main()
