#!/usr/bin/python3



def love_calculator(name1, name2):
    """
    Calculates the love score between two names.

    Args:
        name1: the first name.
        name2: The second name.
    Returns:
        A string representing the love score and a message.
    """
    combined_string = name1.lower() + name2.lower()

    true_count = combined_string.count('t') + combined_string.count('r') + combined_string.count('u') + combined_string.count('e')
    love_count = combined_string.count('l') + combined_string.count('o') + combined_string.count('v') + combined_string.count('e')

    score = int(str(true_count) + str(love_count))

    if score <= 10 or score >= 90:
        return f"Your score is {score} and you go together like coke and mentos"
    elif score >= 40 and score <= 50:
        return f"Your score is {score} and you are alright together"
    else:
        return f"Your score is {score}"




name1 = input("Enter your name: ")
name2 = input("Enter his/her name: ")
print(love_calculator(name1, name2))
print("\n**DISCLAIMER:** This love calculator is for exercises purposes only and does not reflect real-life compatibility. Don't believe that sort of SH*T")
