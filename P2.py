import math

# Three sides of the triangle is x, y and z:
x = float(input("Enter the length of side 'x': "))
y = float(input("Enter the length of side 'y': "))
z = float(input("Enter the length of side 'z': "))

# Calculate the semi perimeter (s)
s = (x + y + z) / 2

# Calculate the area using Heron's formula
area = math.sqrt(s * (s - x) * (s - y) * (s - z))

# calculate the area
print(f"The area of the triangle is: {area:.2f} square units")
