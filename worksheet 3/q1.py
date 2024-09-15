# Write a Python program to calculate the difference between a given number and 17
# with the help of function. If the number is greater than 17, return twice the absolute
# difference. 

def calculate_difference(number):
    if number > 17:
        return 2 * abs(number - 17)
    else:
        return abs(number - 17)

# Example usage
num = int(input("Enter a number: "))
print("Result:", calculate_difference(num))