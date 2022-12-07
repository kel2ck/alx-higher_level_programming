#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared = []
    for i in matrix:
        squared.append([a ** 2 for a in i])
    return squared
