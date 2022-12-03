#! /usr/bin/env python3

with open("input.txt", "r") as file:
    txt = file.read()

compartments = txt.split('\n')

commons = map(lambda x: list(
    set(x[len(x)//2:]) & set(x[:len(x)//2]))[0], compartments)


def get_pri(x):
    return ord(x.lower()) - ord('a') + 1 + (0 if x.islower() else 26)


print(sum(map(lambda x: get_pri(x),  commons)))

commons = map(lambda x: list(set(x[0]) & set(x[1])) &
              set(x[2])[0], list(zip(*(iter(compartments)) * 3)))

print(sum(map(lambda x: get_pri(x), commons)))
