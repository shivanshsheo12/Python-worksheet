#Given a positive integer N. The task is to find 1^2+ 2^2+ 3^2 + ….. + N^2

N = int(input("Enter a number : "))

sum_of_squares = 0

for i in range(1, N + 1):
    sum_of_squares += i**2

print(f"The sum of squares from 1 to {N} is {sum_of_squares}")