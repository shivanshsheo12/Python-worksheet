#Write a Python program to print the even numbers from a given list. Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] Expected Result : [2, 4, 6, 8] 

def print_even_numbers(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    print("Even numbers:", even_numbers)

# Example usage
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print_even_numbers(lst)