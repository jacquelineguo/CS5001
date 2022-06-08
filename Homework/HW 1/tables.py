'''
Xuan Guo
CS 5001, Fall 2020

This program gets the inputs from user about table assembling parts and 
calculates the leftover parts and how many table can be assembled.

Test cases:
60 tops, 244 legs, 500 screws => 60 tables assembled. Leftover parts: 0 table tops, 4 legs, 20 screws.
500 tops, 60 legs, 80 screws => 10 tables assembled. Leftover parts: 490 table tops, 20 legs, 0 screws.
55 tops, 30 legs, 80 screws => 7 tables assembled. Leftover parts: 48 table tops, 2 legs, 24 screws.
'''

def main():
    tops = int(input("Number of tops: "))
    legs = int(input("Number of legs: "))
    screws = int(input("Number of screws: "))
    legs_per_table = 4
    screws_per_table = 8
    num_by_legs = legs // legs_per_table
    num_by_screws = screws // screws_per_table
    tables = min(tops, num_by_legs, num_by_screws)
    top_left = tops - tables
    leg_left = legs - tables * legs_per_table
    screw_left = screws - tables * screws_per_table
    print(str(tables),"tables assembled. Leftover parts:",str(top_left),
    "tops,",str(leg_left), "legs,",str(screw_left),"screws.")

if __name__ == "__main__":
    main()