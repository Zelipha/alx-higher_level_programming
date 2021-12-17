#!/usr/bin/python3
"""Module to divide elaments of a matrix"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix and returns a new matrix
        Args:
            matrix (list): A list of lists of ints or floats.
            div (int/float): The divisor.
        Raise:
             TypeError: if the matrix is not a list of integers or floats
                         if each row of the matrix is not the same size
                         if div is not an int or float
             ZeroDivisionError; if div is equal to 0
    """
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
