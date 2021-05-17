#/usr/bin/python3
"""
functions that prints x elemnt of a list
"""
def safe_print_list(my_list=[], x=0):
    list_len = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end='')
            list_len += 1
        print()
        return (list_len)
    except:
        print()
        return (list_len)
