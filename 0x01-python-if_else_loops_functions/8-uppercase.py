#!/usr/bin/python3
def uppercase(str):
    for c in str:
        x = ord(c)
        if x >= 97 and x <= 122:
            x=x-32
        y = chr(x)
        print(y, end="")
    print()
