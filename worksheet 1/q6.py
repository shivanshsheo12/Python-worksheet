#Write a Python program that accepts a sequence of comma-separated numbers from the
#user and generates a list and a tuple of those numbers. Sample data : 3, 5, 7, 23 

string1 = input("Enter the comma seperated numbers : ")

number_list = [int(x) for x in string1.split(',')]

number_tuple = tuple(number_list)

print("List:", number_list)
print("Tuple:", number_tuple)