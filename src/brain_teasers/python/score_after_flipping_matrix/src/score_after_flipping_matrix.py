"""This module calculate the maximum score of a binary matrix
after row and column flips. The score is calculated by treating
each row of the matrix as a binary number.
"""


def score_after_flipping_matrix(matrix):
    """
    Each row is first made to start with '1', then, for each column, if the number of 0s
    is more than 1s, the column is inverted. The matrix is interpreted as binary numbers
    to calculate the total score.

    Parameters:
    matrix: A 2D binary matrix (list of lists of integers).

    Returns:
    int: Maximum score achievable.
    """
    # Ensure each row starts with 1
    for row in matrix:
        if row[0] == 0:
            row[:] = [1 - x for x in row]

    # Invert columns where necessary
    num_rows = len(matrix)
    for col in range(len(matrix[0])):
        if sum(row[col] for row in matrix) < num_rows / 2:
            for row in matrix:
                row[col] = 1 - row[col]

    # Calculate the total score
    total_score = 0
    for row in matrix:
        total_score += int("".join(map(str, row)), 2)

    return total_score


""" Doctests:
    >>> score_after_flipping_matrix([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]])
    39
    >>> score_after_flipping_matrix([[1, 1, 1], [1, 0, 1], [0, 0, 0]])
    19
    >>> score_after_flipping_matrix([[1]])
    1
"""
