#!/usr/bin/python3
import random # Import the random library for generating random numbers

#Get user input for names
names = input("Enter everybody's name separated by comma: ")

# Split the comma-separated string into a list of names
names_list = names.split(", ")

# Generate a random index within the range of the names list (
random_choice = random.randint(0, len(names_list) - 1)

# Print the result using f-string formatting
print(f"{names_list[random_choice]} will pay the bill")

