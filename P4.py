import math

# Input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the circumference and area
circumference = 2 * math.pi * radius
area = math.pi * radius**2

# Calculated values
print(f"The circumference of the circle is: {circumference:.2f} units")
print(f"The area of the circle is: {area:.2f} square units")

