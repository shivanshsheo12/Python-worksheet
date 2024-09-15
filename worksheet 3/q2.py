#Write a Python program for a function. to test whether a number is within 100 to 1000
#or 2000. 

def is_within_range(number):
    return 100 <= number <= 1000 or number == 2000

# Example usage
num = int(input("Enter a number: "))
print("Is within range:", is_within_range(num))