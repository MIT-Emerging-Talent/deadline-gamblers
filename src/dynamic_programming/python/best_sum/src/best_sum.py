"""
Best Sum Mdule:
This module provides functions to find the shortest combination of numbers from a list that sum up to a given target number.

Note: changing the file name to match the function's name wich must be named "shortest_combination_sum"
requires changing the imported file name in the test file, therefore i didn't want to make changes in the test file.
"""


def find_shortest_combination_sum_basic(
    target: int, numbers: list[int]
) -> list[int] | None:
    """
    Finds the shortest combination of numbers that add up to the target sum using basic recursion.

    The function recursively explores all combinations of numbers that add up to the target sum and returns the shortest such combination.

    Parameters:
    target (int): The target sum.
    numbers (list[int]): A list of integers to be used in combinations.

    Returns:
    list[int] | None: The shortest combination of numbers adding up to the target sum, or None if no combination is possible.

    Assumptions:
    - All numbers in the input list are positive integers.
    - The target is a non-negative integer.

    Doctests:
    >>> find_shortest_combination_sum_basic(7, [5, 3, 4, 7])
    [7]
    >>> find_shortest_combination_sum_basic(8, [2, 3, 5])
    [3, 5]
    >>> find_shortest_combination_sum_basic(0, [1, 2, 3])
    []

    Use Cases:
    - Finding the shortest combination to make change for a given amount.
    - Solving subset sum problems in optimization contexts.

    """
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None

    for num in numbers:
        remainder = target - num
        remainder_combination = find_shortest_combination_sum_basic(remainder, numbers)

        if remainder_combination is not None:
            combination = remainder_combination + [num]
            if shortest_combination is None or len(combination) < len(
                shortest_combination
            ):
                shortest_combination = combination

    return shortest_combination


def find_shortest_combination_sum_memo(
    target: int, numbers: list[int], memo: dict[int, list[int] | None] = None
) -> list[int] | None:
    """
    Finds the shortest combination of numbers that add up to the target sum using memoization to optimize performance.

    This function improves the basic recursive approach by storing previously computed results in a memo dictionary, avoiding redundant computations.

    Parameters:
    target (int): The target sum.
    numbers (list[int]): A list of integers to be used in combinations.
    memo (dict[int, list[int] | None], optional): A dictionary to store computed results for optimization. Defaults to None.

    Returns:
    list[int] | None: The shortest combination of numbers adding up to the target sum, or None if no combination is possible.

    Assumptions:
    - All numbers in the input list are positive integers.
    - The target is a non-negative integer.

    Doctests:
    >>> find_shortest_combination_sum_memo(7, [5, 3, 4, 7])
    [7]
    >>> find_shortest_combination_sum_memo(8, [2, 3, 5])
    [3, 5]
    >>> find_shortest_combination_sum_memo(0, [1, 2, 3])
    []

    Use Cases:
    - Efficiently solving subset sum problems in dynamic programming contexts.
    - Optimizing algorithms for financial calculations, like minimizing coin change.
    """
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None

    for num in numbers:
        remainder = target - num
        remainder_combination = find_shortest_combination_sum_memo(
            remainder, numbers, memo
        )

        if remainder_combination is not None:
            combination = remainder_combination + [num]
            if shortest_combination is None or len(combination) < len(
                shortest_combination
            ):
                shortest_combination = combination

    memo[target] = shortest_combination
    return shortest_combination


def find_shortest_combination_sum_table(
    target: int, numbers: list[int]
) -> list[int] | None:
    """
    Finds the shortest combination of numbers that add up to the target sum using dynamic programming with a table approach.

    This function iteratively builds up a table of solutions for all sums up to the target, providing an efficient solution to the problem.

    Parameters:
    target (int): The target sum.
    numbers (list[int]): A list of integers to be used in combinations.

    Returns:
    list[int] | None: The shortest combination of numbers adding up to the target sum, or None if no combination is possible.

    Assumptions:
    - All numbers in the input list are positive integers.
    - The target is a non-negative integer.

    Doctests:
    >>> find_shortest_combination_sum_table(7, [5, 3, 4, 7])
    [7]
    >>> find_shortest_combination_sum_table(8, [2, 3, 5])
    [3, 5]
    >>> find_shortest_combination_sum_table(0, [1, 2, 3])
    []

    Use Cases:
    - Efficiently solving large subset sum problems in computational finance.
    - Use in dynamic programming education and training for algorithmic efficiency.
    """
    if target < 0:
        return None

    table = [None] * (target + 1)
    table[0] = []

    for i in range(target):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target:
                    combination = table[i] + [num]
                    if table[i + num] is None or len(combination) < len(table[i + num]):
                        table[i + num] = combination

    return table[target]