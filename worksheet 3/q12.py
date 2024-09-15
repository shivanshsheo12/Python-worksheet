#Write a Python class that has two methods: get_String and print_String , get_String
#accept a string from the user and print_String prints the string in upper case.

class StringManipulator:
    def __init__(self):
        self.user_string = ""

    def get_String(self):
        # Accept a string from the user
        self.user_string = input("Enter a string: ")

    def print_String(self):
        # Print the string in upper case
        print(self.user_string.upper())

# Example usage:
string_manipulator = StringManipulator()
string_manipulator.get_String()
string_manipulator.print_String()