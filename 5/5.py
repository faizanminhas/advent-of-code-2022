#! /usr/bin/env python3

with open("input.txt", "r") as file:
    txt = file.read()

towers_in = list(reversed(txt[:txt.index('\n\n')].split('\n')))


def parse_towers(txt):
    towers = [[] for x in txt[0].strip().split('   ')]
    for x in txt[1:]:
        for i in range(0, len(towers)*4, 4):
            if x[i+1] != ' ':
                towers[i//4].append(x[i+1])
    return towers


towers = parse_towers(towers_in)

moves = txt[txt.index('\n\n')+1:].split('\n')

# part1
# for move in moves:
#     if(move.strip() == ''):
#         continue
#     tokens = move.split(' ')
#     num = int(tokens[1])
#     col = int(tokens[3]) - 1
#     to = int(tokens[5]) - 1

#     towers[to] += (reversed(towers[col][-num:]))
#     towers[col] = towers[col][:-num]

for move in moves:
    if(move.strip() == ''):
        continue
    tokens = move.split(' ')
    num = int(tokens[1])
    col = int(tokens[3]) - 1
    to = int(tokens[5]) - 1

    towers[to] += (towers[col][-num:])
    towers[col] = towers[col][:-num]

print(''.join([t[-1] for t in towers]))
