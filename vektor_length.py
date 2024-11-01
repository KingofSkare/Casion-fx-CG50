import math

print("Enter the coordinates of the first point:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
z1 = float(input("z1: "))

print("Enter the coordinates of the second point:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
z2 = float(input("z2: "))

length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
print(f"The length of the vector is: {length}")