'''
Xuan Guo
CS 5001, Fall 2020

This program gets running distance and time from user, then
calculates distance in miles, average pace and speed.

Test cases:
10km, 1 hours, 10 minutes => 6.21 miles,11:16 pace, 5.32 MPH
5km, 0 hours, 30 minutes => 3.11 miles, 9:40 pace, 6.21 MPH
8km, 0 hours, 50 minutes => 4.97 miles, 10:4 pace, 5.96 MPH
'''

def main():
    distance = float(input("How many kilometers did you run? "))
    time_in_hr = int(input("What was your finish time? Enter hours: "))
    time_in_min = int(input("Enter minutes: "))
    km_to_miles = 1.61
    time_convert_rate = 60
    mile = distance / km_to_miles
    total_min = time_in_hr * time_convert_rate + time_in_min
    total_hr = time_in_hr + time_in_min / time_convert_rate
    pace_in_min = int(total_min // mile)
    pace_in_sec = int(round((total_min / mile - pace_in_min) *\
        time_convert_rate, 0))
    speed = round(mile / total_hr, 2)
    print(str(round(mile, 2)), "miles,", str(pace_in_min)+":"+str(pace_in_sec),
    "pace,", str(speed), "MPH")

if __name__ == "__main__":
    main()