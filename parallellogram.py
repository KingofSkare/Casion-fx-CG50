import math

# Function to calculate distance between two points in 3D
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)


# Function to calculate the cross product of two vectors
def cross_product(v1, v2):
    return (
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    )

# Function to calculate the scalar triple product of three vectors
def scalar_triple_product(v1, v2, v3):
    cross_prod = cross_product(v1, v2)
    return cross_prod[0] * v3[0] + cross_prod[1] * v3[1] + cross_prod[2] * v3[2]


# Function to calculate the area of a parallelogram formed by two vectors
# kalkulerer arealet med å ta kryssproduktet av to vektorer
# og deretter regner ut lengden av kryssproduktet
def area_parallelogram(a, b, c, d):
    ab = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
    ac = (c[0] - a[0], c[1] - a[1], c[2] - a[2])
    cross_prod = cross_product(ab, ac)
    area = math.sqrt(cross_prod[0]**2 + cross_prod[1]**2 + cross_prod[2]**2)
    print("Calculated area:",area)  # Debug print
    return area

# Main program
print("Enter the coordinates for the points in the format x y z (separated by spaces)")

# Input for the points
a = tuple(map(float, input("Point A: ").split()))
b = tuple(map(float, input("Point B: ").split()))
c = tuple(map(float, input("Point C: ").split()))

# Calculate point D
# D = C + AB_Vektor
d = (c[0] + (b[0] - a[0]), c[1] + (b[1] - a[1]), c[2] + (b[2] - a[2]))

# Calculate the vectors
ab = (b[0] - a[0], b[1] - a[1], b[2] - a[2])
ac = (c[0] - a[0], c[1] - a[1], c[2] - a[2])
ad = (d[0] - a[0], d[1] - a[1], d[2] - a[2])
bc = (c[0] - b[0], c[1] - b[1], c[2] - b[2])


# Check if the points form a parallelogram
#hvist CD_vector = AB_vector, så er det en parallellogram
if area_parallelogram(a, b, c, d) == 0:
    print("The points are collinear and do not form a parallelogram")
elif (d[0] - c[0], d[1] - c[1], d[2] - c[2]) == (b[0] - a[0], b[1] - a[1], b[2] - a[2]):
    print("The points form a parallelogram")
else:
    print("The points do not form a parallelogram")

# Check if the points are in the same plane
if scalar_triple_product(ab, ac, ad) == 0:
    print("The points are in the same plane")
else:
    print("The points are not in the same plane")
# Print the results
print("Vectors AB:", (b[0] - a[0], b[1] - a[1], b[2] - a[2]))
print("Point D:", d)
print("Vektor AB:", ab)
print("Vektor AC:", ac)
print("Vektor AD:", ad)
print("Vektor BC:", bc)


