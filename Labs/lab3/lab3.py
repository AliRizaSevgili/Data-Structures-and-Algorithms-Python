#
# Author: Ali Riza Sevgili
# Student Number: 135200228
#
# Place the code for your lab 3 here.  Read the specs carefully.  
#
# To test, run the following command :
#     python test_lab3.py
#

def factorial(number):
    # Base case: if the number is 0 or 1, return 1
    if number == 0 or number == 1:
        return 1
    # Recursive case: number * factorial(number - 1)
    else:
        return number * factorial(number - 1)


def linear_search(my_list, key):
    # Loop through each element in the list
    for i in range(len(my_list)):
        # If the current element matches the key, return the index
        if my_list[i] == key:
            return i
    # If the key is not found, return -1
    return -1


def binary_search(my_list, key):
    low = 0
    high = len(my_list) - 1

    # Perform binary search
    while low <= high:
        mid = (low + high) // 2  # Find the middle element
        if my_list[mid] == key:
            return mid  # Key found at index mid
        elif my_list[mid] < key:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Key not found