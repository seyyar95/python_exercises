#!/usr/bin/python3


def first_and_last_the_same(newList):
    """
    Checks if the first and last elements of a list are the same.

    Args:
        newList: The list to check.
    Returns:
        True if the first and last elements are the same, False otherwise.
    """

    # Check if the first and last elements are eqaul
    return newList[0] == newList[-1]



if __name__ == "__main__":
    while True:
        try:
            # Get user input for the list
            userInput = input("Enter an integer list (separate numbers by spaces): ")

            # Check if any digits are consecutive (no spaces)
            if any(num.isdigit() and next_num.isdigit() for num, next_num in zip(userInput, userInput[1:])):
                raise ValueError("Please enter integers separated by spaces.")

            # Convert input to integer list
            newList = list(map(int, userInput.split()))

            break # Exit the loop if input is valid
        except ValueError as e:
            print(f"Error: {e}")

    # Here is the list you entered
    print(f"Given list: {newList}")

    if first_and_last_the_same(newList):
        print(f"The first and last elements of the list are equal")
    else:
        print(f"The first and last elements of the list are not equal")
