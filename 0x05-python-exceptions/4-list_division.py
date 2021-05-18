#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    operation = 0
    list_result = []
    for i in range(0, list_length):
        try:
            operation = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            operation = 0
        except ZeroDivisionError:
            print("division by 0")
            operation = 0
        except IndexError:
            print("out of range")
            operation = 0
        finally:
            list_result.append(operation)
    return (list_result)
