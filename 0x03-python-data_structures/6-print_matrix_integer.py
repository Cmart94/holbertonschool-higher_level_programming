#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len_row = len(matrix)
    if len_row != 1:
        for i in range(len_row):
            len_columns = len(matrix[i])
            for j in range(len_columns):
                if j < len_columns - 1:
                    print("{:d}".format(matrix[i][j]), end=' ')
                else:
                    print("{:d}".format(matrix[i][j]))
    else:
        print()
