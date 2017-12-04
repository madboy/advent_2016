"""
How many IPs in your puzzle input support TLS?

We need an abba sequence inside the supernet,
and none within the hypernet.
"""
import fileinput


def reverse(s: str) -> str:
    return s[::-1]


def abba_sequence(sequence: str) -> bool:
    for i in range(0,len(sequence)-3):
        first = sequence[i:i+2]
        second = sequence[i+2:i+4]
        rsecond = reverse(second)
        if first == rsecond and first != second:
            return True
    return False


def split_address(address: str) -> (list, list):
    hypernet = False
    supernet = []
    hypernets = []
    s = ""
    for c in address:
        if c == "[":
            hypernet = True
            supernet.append(s)
            s = ""
            continue
        elif c == "]":
            hypernet = False
            hypernets.append(s)
            s = ""
            continue
        s += c
    if s:
        supernet.append(s)
    return (supernet, hypernets)


def supports_ipv7(supernets: list, hypernets: list) -> bool:
    for hh in h:
        if abba_sequence(hh):
            return False
    for ss in s:
        if abba_sequence(ss):
            return True

inputs = fileinput.input()

VALID = 0
for line in inputs:
    address = line.strip()
    s, h = split_address(address)
    if supports_ipv7(s, h):
        VALID += 1

print(VALID)
