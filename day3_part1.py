"""
Which are possible triangles?

In a valid triangle, the sum of any two sides must be larger than the remaining side.
"""
import fileinput

def valid_triangle(triangle):
    sides = list(map(int, triangle.split()))
    sides.sort()
    return (sides[0]+sides[1]) > sides[2]

count = 0
for line in fileinput.input():
    triangle = line.strip()
    if valid_triangle(triangle):
        count += 1
print(count)
