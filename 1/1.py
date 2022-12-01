#! /usr/bin/env python3

with open("input.txt", "r") as file:
    txt = file.read()

elves = list(map(lambda x: sum(map(lambda y: int(y) if y != '' else 0, x.split('\n'))), txt.split('\n\n')))

print(f"the max is {max(elves)}")

def top3(l):
    return sorted(l)[-3:]

print(f"the max 3 are {top3(elves)}, total is {sum(top3(elves))}")




