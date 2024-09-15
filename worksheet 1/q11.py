#Write a program to find the euclidean distance between two coordinates

x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))

x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

distance = (((x2 - x1) ** 2 + (y2 - y1) ** 2)**0.5)

print(f"The Euclidean distance between the points ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")