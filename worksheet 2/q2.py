#Write a Python program to sum all the items in a list without using any inbuilt function.

L = [10, 20, 30, 40, 50]
total_sum = 0

for item in L:
    total_sum += item

print(total_sum)