#!/usr/bin/python3

def special_pattern(numbers):
    """
    This function prints a special pattern of numbers in increasing rows.

    Args:
        size: The number of rows in the pattern (must be a positive integer).

    Returns:
        None
    """
    # Loop through each row ( from 1 to size)
    for i in range(1, numbers + 1):
        # Print the current number 'i' repated 'i' times, followed by a space
        print(f"{i} " * i)


while True:
    # Ask user to enter number of rows to print
    numbers = int(input("Enter number of rows to print "))
    if numbers <= 0 or type(numbers) is not int: # Check if the input is correct
        print("The number must be an integer and greater than 0")
    else:
        # Print number of rows based on the user input 
        special_pattern(numbers)
        break

