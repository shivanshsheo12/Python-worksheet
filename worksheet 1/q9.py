#Write a program that will tell whether the number entered by the user is odd or even. 

num = int(input("Enter an integer: "))

if(num%2==0):
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")