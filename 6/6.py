#! /usr/bin/env python3

with open("input.txt", "r") as file:
    txt = file.read().strip()


def unique_seq(seq, n):
    for i in range(n-1, len(seq)):
        if len(set(txt[i-n-1:i])) == n:
            print(i)
            break


unique_seq(4)
unique_seq(14)
