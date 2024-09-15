#User will input (2numbers). Write a program to swap the numbers. Add incrementally
#in any one variable.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

a = a + b 
b = a - b 
a = a - b 

print(f"After swapping: First number is {a}, Second number is {b}")