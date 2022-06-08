'''
Xuan Guo
CS 5001, Fall 2020

This program gets information from user about day of the week and weather, then
creats a workout plan for user.
'''


def main():
    day = input('What day is it? ').lower()
    is_holiday = input('Is it a holiday? ').lower()
    is_rain = input('Is it raining? ').lower()
    temp = float(input('What is the temperature? '))
    VAILD_DAY = ['m', 'tu', 'w', 'th', 'f', 'sa', 'su']
    VAILD_ANS = ['y', 'n']
    WORKOUT_DAY = ['m', 'w', 'f', 'sa']
    RUNNING_DAY = ['m', 'w', 'f']
    TEMP_UPPER = 75
    TEMP_LOWER = 35
    EXERCISE_TIME = 45
    is_valid_input = (day in VAILD_DAY) and (is_holiday in VAILD_ANS) and \
        (is_rain in VAILD_ANS)

    if not is_valid_input or (day in WORKOUT_DAY) or (is_holiday == 'y'):
        if not is_valid_input:
            exercise = 'Swim'
        elif (day in WORKOUT_DAY) or (is_holiday == 'y'):
            if is_rain == 'y':
                exercise = 'Swim'
            elif (is_holiday == 'y') or (day == 'sa'):
                exercise = 'Hike'
            elif (day in RUNNING_DAY) and (is_holiday == 'n'):
                exercise = 'Run'
                if (temp < TEMP_LOWER) or (temp > TEMP_UPPER):
                    EXERCISE_TIME = 30
        print('{} for {} minutes'.format(exercise, EXERCISE_TIME))
    else:
        print('Take a rest day')


if __name__ == '__main__':
    main()
