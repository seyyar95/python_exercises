#!/usr/bin/python3
def remove_chars(word, n):
    """
    Removes the first n chars from a given word and prints the results.

    Args:
        word: The word to modify.
        n: The number of chars to remove from the beginnign of the word.
    Raises:
        ValueError: If n is grater than the length of the word.
    """

    # print the original word for reference
    print(f"Original word: {word}")

    # Create a new string by slicing the word from nth charachter to the end
    x = word[n:]

    # print the modified word with the first n chars removed
    print(x)

    # print the removed chars separately for clarity
    print(f"Removed chars: {word[:n]}")


if __name__ == "__main__":
    # Get user input for the word and the number of chars to remove
    word = input("Enter a word: ")
    n = int(input("Enter number of  chars that you want to remove from the word: "))

    # Validate input to prevent errors
    if n > len(word):
        raise ValueError("Number can't be greater than the length of the word")

    # Call the remove_chars function to perform the modification and printing
    remove_chars(word, n)
