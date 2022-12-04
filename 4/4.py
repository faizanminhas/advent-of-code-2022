#! /usr/bin/env python3

with open("input.txt", "r") as file:
    txt = file.read().strip()

assignments = list(map(lambda x: x.split(','), txt.split('\n')))


def range_contains(a, b):
    [a1, b1] = map(lambda x: int(x), a.split('-'))
    [a2, b2] = map(lambda x: int(x), b.split('-'))

    return (a2 <= a1 and b2 >= b1) or (a1 <= a2 and b1 >= b2)


def weak_range_contains(a, b):
    [a1, b1] = map(lambda x: int(x), a.split('-'))
    [a2, b2] = map(lambda x: int(x), b.split('-'))

    return (a1 <= b2 and b1 >= a2) or (b1 <= a2 and a1 >= b2)


print(sum(map(lambda x: 1 if range_contains(x[0], x[1]) else 0, assignments)))
print(sum(map(lambda x: 1 if weak_range_contains(
    x[0], x[1]) else 0, assignments)))
