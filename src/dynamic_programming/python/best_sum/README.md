
# Shortest Combination Sum Finder / best_sum

## Overview
This module provides efficient solutions for finding the shortest combination of numbers from a list that sum up to a given target. It includes three functions:
1. `find_shortest_combination_sum_basic`
2. `find_shortest_combination_sum_memo`
3. `find_shortest_combination_sum_table`

Each function implements a different approach to solve the problem: basic recursion, memoization, and dynamic programming with a table approach.

## Functions

### 1. `find_shortest_combination_sum_basic`
- **Behavior**: Uses basic recursion to find the shortest combination of numbers that sum up to the target.
- **Strategy**: Explores all combinations and returns the shortest one.
- **Implementation**: Recursive calls for each number subtracted from the target until the target is reached or no combination is possible.
- **Complexity**: Exponential, as it explores every combination without optimization.
  
- **Use Case**:
  ```python
  # Basic Recursion Approach
  result = find_shortest_combination_sum_basic(7, [5, 3, 4, 7])
  print(result) # Output: [7]
  ```

### 2. `find_shortest_combination_sum_memo`
- **Behavior**: Optimizes the basic approach using memoization.
- **Strategy**: Stores results of subproblems to avoid redundant calculations.
- **Implementation**: Similar to the basic approach but uses a memoization dictionary.
- **Complexity**: Significantly reduced compared to basic recursion, though exact complexity depends on the input.

- **Use Case**:
  ```python
  #  Memoization Approach
  result = find_shortest_combination_sum_memo(8, [2, 3, 5])
  print(result) # Output: [3, 5]
  ```

### 3. `find_shortest_combination_sum_table`
- **Behavior**: Utilizes dynamic programming with a table to find the shortest combination.
- **Strategy**: Iteratively builds a solution table for all sums up to the target.
- **Implementation**: Creates a table array and fills it with the shortest combination for each sum leading up to the target.
- **Complexity**: More efficient, particularly for larger target values, with a complexity of O(n*m), where n is the target and m is the number of elements in the list.

  **Use Case**:
  ```python
  # Dynamic Programming Table Approach
  result = find_shortest_combination_sum_table(0, [1, 2, 3])
  print(result) # Output: []
  ```

## Run the Test:
Open a terminal or command prompt, navigate to the `best_sum` directory and run the following command line

```pash
python -m unittest discover -v
```

## Conclusion
This module offers three distinct approaches to solving the subset sum problem, each with its own trade-offs in terms of complexity and efficiency. The basic recursion is straightforward but less efficient, memoization offers a balance, and the table approach is the most efficient for larger datasets.