#! /usr/bin/env python3

with open("input.txt", "r") as file:
    txt = file.read()

rounds = txt.split('\n')

def letterScore(c):
    return ord(c) - ord('W')

def game(m1, m2):
    if ord(m1) + 23 == ord(m2):
        return 3 + letterScore(m2)
    else:
        if m1 == 'A':
            if m2 == 'Y':
                return 6 + letterScore(m2)
            elif m2 == 'Z':
                return 0 + letterScore(m2)
        elif m1 == 'B':
            if m2 == 'Z':
                return 6 + letterScore(m2)
            elif m2 == 'X':
                return 0 + letterScore(m2)
        elif m1 == 'C':
            if m2 == 'X':
                return 6 + letterScore(m2)
            elif m2 == 'Y':
                return 0 + letterScore(m2)

def game2(m1, m2):
    if m1 == 'A':
        if m2 == 'X':
            return 0 + letterScore('Z')
        elif m2 == 'Y':
            return 3 + letterScore('X')
        elif m2 == 'Z':
            return 6 + letterScore('Y')
    elif m1 == 'B':
        if m2 == 'X':
            return 0 + letterScore('X')
        elif m2 == 'Y':
            return 3 + letterScore('Y')
        elif m2 == 'Z':
            return 6 + letterScore('Z')
    elif m1 == 'C':
        if m2 == 'X':
            return 0 + letterScore('Y')
        elif m2 == 'Y':
            return 3 + letterScore('Z')
        elif m2 == 'Z':
            return 6 + letterScore('X')

print(f"score is {sum(map(lambda x: game2(x[0], x[2]), rounds))}")