#!/usr/bin/python3
size = input("What size pizza would you like(S/M/L)? ")
bill = 0
if size == "S" or size == "s":
    print("Small Pizza price is 15 AZN")
    bill += 15
elif size == "M" or size == "m":
    print("Medium Pizza price is 22 AZN")
    bill += 22
elif size == "L" or size =="l":
    print("Large Pizza price is 30 AZN")
    bill += 30
else:
    print("You have only three option. Please choose one")

add_pepperoni = input("Do you want pepperoni(Y/N)? ")
if add_pepperoni == "Y" or add_pepperoni == "y":
    if size == "S" or size == "s":
        bill += 2
    else:
        bill += 5

extra_cheese = input("Do you want extra cheese(Y/N)? ")
if extra_cheese == "Y" or extra_cheese == "y":
    bill += 8

print(f"Your final bill is {bill}")
