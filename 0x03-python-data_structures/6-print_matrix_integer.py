#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print("{:d}".format(matrix[i][j]), end="")
            if j != (len(matrix[i]) - 1):
                print(" ", end="")
        print("")
