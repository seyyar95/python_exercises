#!/usr/bin/python3

# Prompt user to enter a word.
word = input("Enter a word: ")

# Print the original word to reference.
print(f"Original word: {word}")

# Print a message indicating the purpose of the followoing code
print(f"Printing only even index chars")

# Iterate through each character in the word
for char in range(len(word)):
    # Check if the current character index is even (divisible by 2)
    if char % 2 == 0:
        # If it is even, print the character at that index
        print(word[char])



"""
Solution 2:
    even_chars = [word[i] for i in range(0, len(word), 2)]
    print("".join(even_chars))
"""
