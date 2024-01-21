# Quick Sort Module

## Overview

The `quick_sort` module provides two versions of the quicksort algorithm, offering efficient and versatile ways to sort arrays in Python. Both versions implement the quicksort algorithm to sort arrays of numbers in ascending order but differ slightly in their approaches.

## Implementations

### 1. `quicksort_v1`

- **Behavior**: Sorts an array using the quicksort algorithm. This version chooses the last element as the pivot and recursively sorts the elements.
- **Strategy**: The function divides the array into two sub-arrays: elements less than the pivot and elements greater than the pivot. It then recursively applies the same strategy to these sub-arrays.

#### Usage

```python
from quick_sort import quicksort_v1

# Example 1: Sorting an empty array
print(quicksort_v1([]))  # Output: []

# Example 2: Sorting a random array
print(quicksort_v1([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Example 3: Sorting a descending array
print(quicksort_v1([5, 4, 3, 2, 1]))  # Output: [1, 2, 3, 4, 5]
```


### 2. `quicksort_v2`
- **Behavior:** Sorts an array using a different implementation of the quicksort algorithm.
- **Strategy:** This version uses a partitioning method where elements are rearranged based on their comparison with the pivot. The function then recursively sorts the sub-arrays created by the partition.

```python
from quick_sort import quicksort_v2

# Example 1: Sorting an empty array
print(quicksort_v2([]))  # Output: []

# Example 2: Sorting a random array
print(quicksort_v2([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Example 3: Sorting a descending array
print(quicksort_v2([5, 4, 3, 2, 1]))  # Output: [1, 2, 3, 4, 5]
```
## Testing Code Implementation:
Run the following command in the directory `quick_sort`
```pash
python -m unittest discover -v
```

## Conclusion
The `quick_sort` module offers two efficient and easy-to-use implementations of the quicksort algorithm, suitable for a variety of sorting needs. The different strategies employed by `quicksort_v1` and `quicksort_v2` provide flexibility in choosing an approach that best fits the specific use case.