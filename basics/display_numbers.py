#!/usr/bin/python3
def find_divisible_by_5(num_list):
    """
    Prints numbers from a list that are divisible by 5.
    """
    print("Divisible by 5:")
    divisible_numbers = [num for num in num_list if num % 5 == 0]
    print(*divisible_numbers, sep="\n") # Print each number on a new line

if __name__ == "__main__":
    while True:
        try:
            nums = input("Enter an integer list: ")
            num_list = list(map(int, nums.split()))
            break # Exit the loop if input is valid
        except Exception as e:
            print(f"Error: {e}")

    find_divisible_by_5(num_list)
