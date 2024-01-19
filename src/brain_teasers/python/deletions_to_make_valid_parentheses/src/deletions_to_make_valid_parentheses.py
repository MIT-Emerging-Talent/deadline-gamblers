"""
Module: deletions_to_make_valid_parentheses

This module provides a function to calculate the minimum number of deletions required to balance parentheses in a given input string.

"""


def deletions_to_make_valid_parentheses(input_string):
    """
    Calculate the minimum number of deletions required to balance parentheses in a given input string.

    Parameters:
        input_string (str): The input string containing parentheses.

    Returns:
        int: The minimum number of deletions required to balance the parentheses.
    """
    stack = []
    deletions = 0

    for char in input_string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                deletions += 1
            else:
                stack.pop()

    deletions += len(stack)
    return deletions
