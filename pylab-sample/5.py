#Solve a trianles area, given 2 sides and not included an angle.
import math

# Input the lengths of the two sides and the included angle in degrees
a = float(input("Enter the length of side 'a': "))
b = float(input("Enter the length of side 'b': "))
angle_degrees = float(input("Enter the included angle in degrees: "))

# Convert the angle from degrees to radians
angle_radians = math.radians(angle_degrees)

# Calculate the area of the triangle
area = 0.5 * a * b * math.sin(angle_radians)

print(f"The area of the triangle is: {area}")
