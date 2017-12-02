"""
sum of sectorids

A room is real (not a decoy) if the checksum is the five most common letters in 
the encrypted name, in order, with ties broken by alphabetization.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.
"""
import fileinput
from collections import defaultdict

def real_room(letters, checksum):
    count = defaultdict(int)
    for letter in letters:
        count[letter] += 1
    ordered = sorted(count.items(), key=lambda t: t[1])
    for letter in checksum:
        o = ordered.pop()
        # which character we popped doesn't matter we only care
        # about that it has the correct number of occurences
        if count[letter] == o[1]:
            continue
        else:
            return False
    return True

total = 0
for line in fileinput.input():
    room = line.strip()
    parts = room.split("-")
    letters = parts[:-1]
    sectorid, checksum = parts[-1].split("[")
    checksum = checksum.strip("]")
    if real_room("".join(letters), checksum):
        total += int(sectorid)

print(total)
