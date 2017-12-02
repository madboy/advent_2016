"""
santas secret room
"""
import fileinput

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
indices = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
ai = dict(zip(alpha, indices))


def decrypt_room(letters, count):
    fwd = count%26
    room_name = ""
    for letter in letters:
        if letter == " ":
            room_name += letter
            continue
        index = (ai[letter] + fwd) % 26
        room_name += alpha[index]
    return room_name


for line in fileinput.input():
    room = line.strip()
    room = room.split("-")
    encrypted = room[:-1]
    sectorid = room[-1].split("[")[0]
    room_name = decrypt_room(" ".join(encrypted), int(sectorid))
    if "pole" in room_name:
        print(room_name, sectorid)
