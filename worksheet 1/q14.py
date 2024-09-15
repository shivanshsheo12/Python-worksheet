# Given a positive integer N, the task is to write a Python program to check if the number
# is Prime or not in Python.

N = int(input("Enter a number for prime check : "))

t = N**0.5
d = 2
while(d<=t):
    if N%d==0:
        break
    d+=1
if d>t:
    print(f"{N} is a prime number")
else:
    print(f"{N} is not a prime number")