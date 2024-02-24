#!/usr/bin/python3
"""
This program calculates the sum of consecutive numbers from 1 to 10,
printing the current number, previous number, and sum at each step.
"""

previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    # Calculate the sum of the current and previous numbers
    result = previous_num + i

    # Print the results 
    print(f"Current Number: {i}\nPrevious Number: {previous_num}\nSum: {result}")

    # update the previous number for the next iteration
    previous_num = i
