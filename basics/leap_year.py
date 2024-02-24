#!/usr/bin/python3

# a pyhton script that checks if the given year is leap or not
# Usage: leap_year.py <year>

year = int(input("Which year you want to check? "))
# This line prompts the user to enter a year and converts the input to an integer.

if year % 4 == 0:
    # Check if the year is divisible by 4, which is a basic requirement for a leap year.

    if year % 100 == 0:
        # if the year is divisible by 4, further check if it's divisible by 100
        # centuries are not leap years unless they are also divisible by 400.

        if year % 400 == 0:
            # if the year is divisible by 100 and 400, it is a leap year.
            print(f"{year} is a leap year")
        else:
            # if the year is divisible by 100 but not 400, it is not a leap year.
            print(f"{year} is not a leap year")
    else:
        # if the year is divisible by 4 but not 100, it is a leap year.
        print(f"{year} is a leap year")
else:
    # if the year is not divisible by 4, it is not a leap year.
    print(f"{year} is not a leap year")
