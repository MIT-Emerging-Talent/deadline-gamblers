# `all_combinations` Module

## Overview

The `all_combinations` module provides a utility function to generate all possible combinations of a specified size from a range of numbers. This function is useful in various scenarios, such as generating combinations for lottery systems or determining all possible team matchups in a tournament.

## Function Documentation

### `all_combinations(n: int, k: int) -> List[List[int]]`

This function generates all possible combinations of size `k` from the numbers 0 to `n` (inclusive).

#### Parameters:

- `n (int)`: The upper limit of the range (inclusive).
- `k (int)`: The size of each combination.

#### Returns:

- `List[List[int]]`: A list of all combinations, where each combination is a list of integers.

#### Assumptions:

- Both `n` and `k` are non-negative integers.
- The range of numbers is from 0 to `n`, inclusive.

## Implementation

The function utilizes the `itertools.combinations` method from Python's standard library to generate the required combinations. It iterates over a range of numbers from 0 to `n`, inclusive, and produces combinations of size `k`.

## Usage Examples

The following examples illustrate how to use the `all_combinations` function:

1. **Generating Single-Digit Combinations**:
    ```python
    # Generate combinations of 1 digit from 0 to 2
    combinations = all_combinations(2, 1)
    print(combinations) # Output: [[0], [1], [2]]
    ```

2. **Generating Pair Combinations**:
    ```python
    # Generate combinations of 2 digits from 0 to 4
    combinations = all_combinations(4, 2)
    print(combinations) # Output: [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    ```

3. **Empty Combination Case**:
    ```python
    # Generate an empty combination
    combinations = all_combinations(0, 0)
    print(combinations) # Output: [[]]
    ```
## Run the Test:
Open a terminal or command prompt, navigate to the `all_combination` directory and run the following command line
```pash
 python -m unittest discover -v
 ```
## Use Cases

1. **Lottery System**: Generating all possible lottery number combinations.
2. **Tournament Matchups**: Generating all possible team matchups in a sports tournament.

This module is straightforward to integrate and use, making it suitable for a wide range of applications that require combination generation.
