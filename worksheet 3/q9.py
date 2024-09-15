#Write a Python class named Student with two attributes: student_id, student_name. Add
#a new attribute: student_class. Create a function to display all attributes and their values
#in the Student class. 

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_class = None  # Add a new attribute: student_class

    def display_attributes(self):
        # Display all attributes and their values
        attributes = vars(self)
        for attribute, value in attributes.items():
            print(f"{attribute}: {value}")


# Create a Student object
student1 = Student(1, "John Doe")
student1.student_class = "10th Grade"
student1.display_attributes()