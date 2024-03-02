#!/usr/bin/python3

# This script takes pizza order and calculates the total bill

# Get the desired pizza size from the user
size = input("What size pizza would you like(S/M/L)? ").lower() # Convert input to lowercase for case-insensitive comparison

bill = 0 # Initialize the bill amount

# Check the pizza size and update the bill accordingly
if size in ("s", "m", "l"): # Check if size is one of the valid options (S, M or L)
    if size == "s":
        print("Small Pizza price is 15 AZN")
        bill += 15
    elif size == "m":
        print("Medium Pizza price is 22 AZN")
        bill += 22
    elif size =="l":
        print("Large Pizza price is 30 AZN")
        bill += 30
    else:
        print("You have only three option. Please choose one")

else:
    print("You have only three options. Please choose one (S, M or L)") # Handle invalid input for Pizza size

# Ask if the user wants pepperoni
ad_pepperoni = input("Do you want pepperoni(Y/N)? ").lower() # Convert input to lowercase for case-insensitive comparison

# Add pepperoni cost based on size
if add_pepperoni in ("y", "n"): # Check if input is valid (Y or N)
    if add_pepperoni == "y":
        if size == "s":
            bill += 2
        else:
            bill += 5
else:
    print("Invalid input. Please answer Y or N") # Handle invalid input for pepperoni

# ask if the user wants extra cheese
extra_cheese = input("Do you want extra cheese(Y/N)? ").lower() # Convert input to lowercase for case-insensitive comparison

# Add extra cheese cost
if extra_cheese in ("y", "n"): # Check if input is valid (Y or N)
    if extra_cheese == "y":
        bill += 8
else:
    print("Invalid input. Please answer Y or N") # Handle invalid input for extra cheese

# Print the final bill amount
print(f"Your final bill is {bill} AZN")
