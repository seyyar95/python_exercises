#!/usr/bin/python3

def merge_list(list1, list2):
    result_list = []

    # iterate first list
    for num in list1:
        # check if current number is odd
        if num % 2 != 0:
            # add odd number to result list
            result_list.append(num)

    # iterate second list
    for num in list2:
        # check if current number is even
        if num % 2 == 0:
            # add even number to result list
            result_list.append(num)

    return sorted(result_list)



list1 = input("Enter first list (integers only): ")
list2 = input("Enter second list (integers only): ")

numbers_of_list1 = list(map(int, list1.split()))
numbers_of_list2 = list(map(int, list2.split()))

print("result list: ", merge_list(numbers_of_list1, numbers_of_list2))
