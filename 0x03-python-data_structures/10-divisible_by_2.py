def divisible_by_2(my_list=[]):
    return_list = []
    for i in my_list:
        if i % 2 == 0:
            return_list.append(True)
        else:
            return_list.append(False)
    return (return_list)
