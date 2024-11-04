import math

def isclose(a, b, rel_tol=1e-9):
    return abs(a - b) <= rel_tol * max(abs(a), abs(b))

# Prompt user for coordinates
print("Enter the coordinates of the first point (A):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
z1 = float(input("z1: "))

print("Enter the coordinates of the second point (B):")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
z2 = float(input("z2: "))

print("Enter the coordinates of the third point (C):")
x3 = float(input("x3: "))
y3 = float(input("y3: "))
z3 = float(input("z3: "))

AB_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
AC_length = math.sqrt((x3 - x1)**2 + (y3 - y1)**2 + (z3 - z1)**2)
BC_length = math.sqrt((x3 - x2)**2 + (y3 - y2)**2 + (z3 - z2)**2)

print("AB length:", AB_length)
print("AC length:", AC_length)
print("BC length:", BC_length)

if isclose(AB_length**2 + AC_length**2, BC_length**2, rel_tol=1e-9):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")

print("AB_length**2 + AC_length**2:", AB_length**2 + AC_length**2)
print("BC_length**2:", BC_length**2)