"""
Given the recording in your puzzle input, what is the error-corrected version of the message being sent?

Correct characters are the _LEAST_ common ones in each column.
"""
import argparse
import fileinput
from collections import defaultdict

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", action="store_true")
parser.add_argument("file")
args = parser.parse_args()

if args.test:
    INPUT = [
        "eedadn",
        "drvtee",
        "eandsr",
        "raavrd",
        "atevrs",
        "tsrnev",
        "sdttsa",
        "rasrtv",
        "nssdts",
        "ntnada",
        "svetve",
        "tesnvt",
        "vntsnd",
        "vrdear",
        "dvrsen",
        "enarar",
    ]
else:
    INPUT = fileinput.input()

def create_counted(columns):
    for _ in range(0, columns):
        counted.append(defaultdict(int))

counted = []
for line in INPUT:
    word = line.strip()
    if not counted:
        create_counted(len(word))
    for i, character in enumerate(word):
        counted[i][character] += 1

error_corrected = ""
for counts in counted:
    current_max = 0
    correct_character = ""
    for character, count in counts.items():
        if count > current_max:
            correct_character = character
            current_max = count
    error_corrected += correct_character
print(error_corrected)
