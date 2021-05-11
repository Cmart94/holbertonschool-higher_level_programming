#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return (None)
    max_int = my_list[0]
    for i in my_list:
        if max_int < i:
            max_int = i
    return (max_int)
