#!/usr/bin/python3

"""
This function performs multipilication or sum based on a condition.

Args:
    n1: The first number.
    n2: The second number.
Returns:
    The product of n1 and n2 if it is less than or equal to 1000, otherwise the sum of n1 and n2.
"""


def multipilication_or_sum(n1, n2):
    product = n1 * n2

    if product <= 1000:
        return product
    else:
        return n1 + n2


# test cases with different inputs
result = multipilication_or_sum(50, 70)
print(f"The result is: {result}")

result = multipilication_or_sum(15, 10)
print(f"The result is: {result}")
