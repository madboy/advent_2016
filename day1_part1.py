"""
N (l <-, r ->)
E (l ^, r .)
S (l ->, r <-)
W (l ., r ^)
"""
FACES = [
    ("N", (-1, 1), (0, 0)),
    ("E", (0, 0), (1, -1)),
    ("S", (1, -1), (0, 0)),
    ("W", (0, 0), (-1, 1))
]


def blocks(loc1, loc2):
    return abs(loc1[0]-loc2[1]) + abs(loc1[1]-loc2[1])


def new_pos(current, instruction, facing=None):
    f, x, y =  FACES[facing]
    cx, cy = current    
    direction, distance = instruction[0], int(instruction[1:])
    if direction == "R":
        facing = (facing + 1) % 4
        xsign, ysign = x[1], y[1]
    else:
        facing = (facing - 1) % 4
        xsign, ysign = x[0], y[0]        
    
    return (cx+xsign*distance,cy+ysign*distance), facing


instructions = "L2, L3, L3, L4, R1, R2, L3, R3, R3, L1, L3, R2, R3, L3, R4, R3, R3, L1, L4, R4, L2, R5, R1, L5, R1, R3, L5, R2, L2, R2, R1, L1, L3, L3, R4, R5, R4, L1, L189, L2, R2, L5, R5, R45, L3, R4, R77, L1, R1, R194, R2, L5, L3, L2, L1, R5, L3, L3, L5, L5, L5, R2, L1, L2, L3, R2, R5, R4, L2, R3, R5, L2, L2, R3, L3, L2, L1, L3, R5, R4, R3, R2, L1, R2, L5, R4, L5, L4, R4, L2, R5, L3, L2, R4, L1, L2, R2, R3, L2, L5, R1, R1, R3, R4, R1, R2, R4, R5, L3, L5, L3, L3, R5, R4, R1, L3, R1, L3, R3, R3, R3, L1, R3, R4, L5, L3, L1, L5, L4, R4, R1, L4, R3, R3, R5, R4, R3, R3, L1, L2, R1, L4, L4, L3, L4, L3, L5, R2, R4, L2"

start = (0, 0)
facing = 0
current = start

for instruction in instructions.split(","):
    instruction = instruction.strip()
    current, facing = new_pos(current, instruction, facing)

print(current)
print(blocks(current, start))


