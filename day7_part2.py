"""
How many IPs in your puzzle input support SSL?

We need an aba sequence inside a supernet sequence,
and a bab within the hypernet.
"""
import fileinput


def reverse(s: str) -> str:
    return s[::-1]


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


def aba_sequence(sequence: str) -> list:
    abas = []
    for c in range(0, len(sequence)-2):
        aba = sequence[c:c+3]
        if aba == reverse(aba) and aba[1] != aba[0]:
            abas.append(aba)
    return abas


def supports_ssl(supernets: list, hypernets: list) -> bool:
    abas = []
    for supernet in supernets:
        abas.extend(aba_sequence(supernet))

    for hypernet in hypernets:
        for aba in abas:
            bab = aba[1] + aba[0] + aba[1]
            if bab in hypernet:
                return True
    return False

inputs = fileinput.input()

VALID = 0
for line in inputs:
    address = line.strip()
    s, h = split_address(address)
    if supports_ssl(s, h):
        VALID += 1

print(VALID)
