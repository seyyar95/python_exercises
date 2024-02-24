#!/usr/bin/python3

def count_substring(statement, substring):
    """
    Counts the number of occurrences of a substring within a string.

    Args:
        statement: The string to search within.
        substring: The substring to search for.

    Returns:
        The number of times the substring appears in the statement.
    """
    # Print informative messages about the input
    print(f"Given string: {statement}\nSubstring to search for: {substring}")

    count = 0
    
    # Iterate through potential starting indices of the substring in the statement
    for i in range(len(statement) - len(substring) + 1):
        # increment count if a match is found
        count += statement[i:i + len(substring)] == substring

    return count # Return the total count of occurrences


if __name__ == "__main__":
    # Get user input for the string and substring
    statement = input("Enter a string: ")
    substring = input("enter a substring to search for: ")

    # Call the function to find the count of occurrences
    count = count_substring(statement, substring)

    # Print the result based on the count
    if count > 0:
        print(f'The substring "{substring}" appears {count} times in the string.')
    else:
         print(f'The substring "{substring}" is not found in the string.')
