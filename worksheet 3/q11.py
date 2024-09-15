#Write a Python class named Circle constructed from a radius and two methods that will compute the area and the perimeter of a circle

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Compute the area of the circle
        return math.pi * self.radius ** 2

    def perimeter(self):
        # Compute the perimeter (circumference) of the circle
        return 2 * math.pi * self.radius

# Example usage:
circle = Circle(5)
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())