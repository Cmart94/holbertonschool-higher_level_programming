#!/usr/bin/python3
for i in range(0, 9):
    for j in range(0, 10):
        if i == j:
            continue
        elif j < i:
            continue
        elif i == 8 and j == 9:
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}".format(i, j), end=", ")
