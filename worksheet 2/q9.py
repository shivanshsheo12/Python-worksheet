#Iterate the given list of numbers and print only those numbers which are divisible by 5.

numbers = [10, 23, 45, 67, 80, 91, 100, 112]
for number in numbers:
    if number % 5 == 0:
        print(number)