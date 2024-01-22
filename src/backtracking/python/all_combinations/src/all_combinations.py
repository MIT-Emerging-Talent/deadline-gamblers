"""
Module: all_combinations

This module provides a function to generate all possible combinations of a specified size from a range of numbers.
"""

from typing import List
import itertools


def all_combinations(n: int, k: int) -> List[List[int]]:
    """
    Generate all combinations of size 'k' from numbers 0 to 'n'.

    Parameters:
    n (int): The upper limit of the range (inclusive).
    k (int): The size of each combination.

    Returns:
    List[List[int]]: A list of all combinations, where each combination is a list of integers.

    Assumptions:
    - 'n' and 'k' are non-negative integers.
    - The range is from 0 to 'n' inclusive.

    Doctests:
    >>> all_combinations(2, 1)
    [[0], [1], [2]]

    >>> all_combinations(4, 2)
    [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

    >>> all_combinations(0, 0)
    [[]]

    Use cases:
    - Generating combinations for a lottery system.
    - Generating all team matchups in a tournament.
    """
    # Generating combinations using itertools.combinations
    return [list(comb) for comb in itertools.combinations(range(n + 1), k)]
