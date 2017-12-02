from collections import namedtuple
import fileinput

"""What is the bathroom code?

1 2 3
4 5 6
7 8 9

U, D = change row
L, R = change column
"""

Key = namedtuple('Key', ['row', 'col'])

KEYPAD = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

def get_button(key, instruction):
    for move in instruction:
        if move == "U":
            key = key._replace(row=max(key.row - 1, 0))
        elif move == "D":
            key = key._replace(row=min(key.row + 1, 2))
        elif move == "L":
            key = key._replace(col= max(key.col - 1, 0))
        elif move == "R":
            key = key._replace(col=min(key.col + 1, 2))            
    return key


code = ""
key = Key(1,1)
for instruction in fileinput.input():
    instruction = instruction.strip()
    key = get_button(key, instruction)
    code += KEYPAD[key.row][key.col]
print(code)
