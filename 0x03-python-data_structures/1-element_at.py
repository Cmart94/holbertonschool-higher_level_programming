#!/usr/bin/python3
def element_at(my_list, idx):
    list_len = len(my_list)
    if idx > list_len - 1 or idx < 0:
        return None
    else:
        r = my_list[idx]
        return (r)
