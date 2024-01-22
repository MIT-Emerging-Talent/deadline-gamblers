# Sum of subarray

Python function to sum the elements of a subarray of an input array.

```python
# function:
subarray_sum(arr, start_index, end_index)

# parameters
arr: an array of numeric values
start_index: starting index of the subarray
end_index: ending index of the subarray
```

This function takes an array as input with all elements as numeric, makes a sub-array based the start and end indices, and returns the sum of the sub-array.

```python
subarray_sum([0, 0, 0, 0], 0, 3)
output: 0

subarray_sum([10, 0, 0, 0], 1, 3)
output: 0

subarray_sum([10, 0, 0, 10], 0, 3)
output: 10

subarray_sum([10, 0, 0, 10], 0, 4)
output: 20

subarray_sum([10, 10, 10, 10], 1, 3)
output: 20
```
