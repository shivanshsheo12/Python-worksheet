#Write a Python class named Student with two instances student1, student2 and assign
#values to the instances' attributes. Print all the attributes of the student1, student2
#instances with their values in the given format.

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

# Create two instances of the Student class
student1 = Student(1, "Ansh")
student2 = Student(2, "Vansh")

# Print all attributes of both instances
print("Student 1:")
for attribute, value in vars(student1).items():
    print(f"{attribute}: {value}")

print("\nStudent 2:")
for attribute, value in vars(student2).items():
    print(f"{attribute}: {value}")