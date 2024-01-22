
# Score After Flipping Matrix

This module calculates the maximum score achievable by flipping rows and columns of a binary matrix.

## Solution Overview

The `score_after_flipping_matrix` function is designed to optimize the score of a given binary matrix. The score is calculated by interpreting each row of the matrix as a binary number. The optimization is done by flipping rows and columns under certain conditions to maximize the overall score.

### Strategy

The strategy for maximizing the matrix's score has two main steps:

1. **Row Flipping**: Each row in the matrix is checked, and if a row doesn't start with a `1`, it's flipped. This step ensures that the most significant bit of each binary number (row) is maximized.

2. **Column Analysis**: For each column, starting from the left (after the first column), the function counts the number of `1`s. If the count of `0`s in any column is greater than the count of `1`s, that column is virtually flipped to maximize the score. The function then calculates the score based on the optimized matrix.

### Implementation

The implementation is done in Python, with clear and concise code. It includes type annotations for better readability and maintenance. The function adheres to the principle of simplicity and clarity in its strategy.

```python
def score_after_flipping_matrix(matrix):
    # Function implementation
```

## Usage

The function can be used directly with any 2D binary matrix. Here are some use cases demonstrating its behavior:

### Use Case 1

```python
matrix = [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
print(score_after_flipping_matrix(matrix))
# Output: 39
```

### Use Case 2

```python
matrix = [[1, 1, 1], [1, 0, 1], [0, 0, 0]]
print(score_after_flipping_matrix(matrix))
# Output: 19
```

### Use Case 3

```python
matrix = [[1]]
print(score_after_flipping_matrix(matrix))
# Output: 1
```

## Testing Code Implementation:
Run the following command in the directory `score_after_flipping_matrix`
```pash
python -m unittest discover -v
```

## Conclusion

The `score_after_flipping_matrix` function provides a robust solution for maximizing the score of a binary matrix. Its implementation is straightforward, focusing on readability and efficiency.