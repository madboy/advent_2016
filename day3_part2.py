"""
Which are possible triangles?

In a valid triangle, the sum of any two sides must be larger than the remaining side.
"""
import fileinput

def valid_triangle(sides):
    sides.sort()
    return (sides[0]+sides[1]) > sides[2]

count = 0
row = 0
triangles = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
]
for line in fileinput.input():
    cols = line.strip()
    sides = list(map(int, cols.split()))
    triangles[0][row] = sides[0]
    triangles[1][row] = sides[1]
    triangles[2][row] = sides[2]
    if row == 2:
        for triangle in triangles:
            if valid_triangle(triangle):
                count += 1
        row = -1
    row += 1

print(count)
