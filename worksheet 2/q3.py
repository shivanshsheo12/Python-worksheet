#Write a Python program to multiply all the items in a list without using any inbuilt function.

L = [1, 2, 3, 4, 5]
product = 1

for item in L:
    product *= item

print(product)