# Create a new list from two list using the following condition, Given two list of numbers, write
# a program to create a new list such that the new list should contain odd numbers from the first
# list and even numbers from the second list.

list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 11, 12, 13, 14, 15]

odd_numbers_from_list1 = [num for num in list1 if num % 2 != 0]
even_numbers_from_list2 = [num for num in list2 if num % 2 == 0]

new_list = odd_numbers_from_list1 + even_numbers_from_list2

print("New list:", new_list)