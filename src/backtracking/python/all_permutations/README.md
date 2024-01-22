# Permutations Generator

This Python module provides a function to generate all permutations of a given list of elements using a backtracking algorithm.

## Installation

No installation is required. Simply include the `permutations.py` file in your project and import the `all_permutations` function.

## Implementation Details
The function is implemented using a recursive backtracking algorithm. The main function initializes an empty list to store the permutations and calls a helper function, generate_permutations_backtracking, with the initial parameters.

## Example
    elements = [1, 2, 3]
    permutations = all_permutations(elements)
    print(permutations)
Output will be:
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]