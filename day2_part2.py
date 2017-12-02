from collections import namedtuple
import fileinput

"""What is the bathroom code?

    1
  2 3 4
5 6 7 8 9
  A B C
    D

U, D = change row
L, R = change column
"""

Key = namedtuple('Key', ['row', 'col'])

KEYPAD = [
    ["-", "-", "1", "-", "-"],
    ["-", "2", "3", "4", "-"],
    ["5", "6", "7", "8", "9"],
    ["-", "A", "B", "C", "-"],
    ["-", "-", "D", "-", "-"],
]

def valid(candidate, origin):
    """Determine if we have a valid key on the keypad

    If we have moved to an uassigned key we will return the original key
    since we cannot make a valid move
    """
    if KEYPAD[candidate.row][candidate.col] == "-":
        return origin
    return candidate
    
def get_button(key, instruction):
    temp = None
    for move in instruction:
        if move == "U":
            temp = key._replace(row=max(key.row - 1, 0))
        elif move == "D":
            temp = key._replace(row=min(key.row + 1, 4))
        elif move == "L":
            temp = key._replace(col= max(key.col - 1, 0))
        elif move == "R":
            temp = key._replace(col=min(key.col + 1, 4))
        key = valid(temp, key)        
    return key


code = ""
key = Key(2,0)
for instruction in fileinput.input():
    instruction = instruction.strip()
    key = get_button(key, instruction)
    code += KEYPAD[key.row][key.col]
print(code)
