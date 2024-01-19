# Merge Sort  
This module provides two functions for performing merge sort on arrays.

## Examples
here's an example of how you might use these functions:


```python
# Create an unsorted list
unsorted_list = [5, 1, 9, 3, 7]

# Use the mergesort_v1 function to sort the list
sorted_list_v1 = merge_sort_module.mergesort_v1(unsorted_list)
print("Sorted list using mergesort_v1: ", sorted_list_v1)

# Use the mergesort_v2 function to sort the list
sorted_list_v2 = merge_sort_module.mergesort_v2(unsorted_list)
print("Sorted list using mergesort_v2: ", sorted_list_v2)
```

```python
Input:

unsorted_list = [5, 1, 9, 3, 7]

Output:

Sorted list using mergesort_v1:  [1, 3, 5, 7, 9]
Sorted list using mergesort_v2:  [1, 3, 5, 7, 9]
```

## Approach

There are two different approaches to solve this problem:

* `mergesort_v1()`: This function implements the merge sort algorithm recursively. It takes an array as input and divides it into halves until the base case is reached (when the array length is 1 or less). Then, it merges the sorted halves using the merge function and returns the sorted array.

* `mergesort_v2()`: This function implements the merge sort algorithm in Python. The mergesort_v2 function takes an array as input and recursively divides it into smaller subarrays until each subarray contains only one element. It then merges these subarrays back together in sorted order. The _merge_sort function is a helper function that performs the actual sorting. The sorted array is returned as the output of the mergesort_v2 function.


## Unittest results
test command:
```
merge_sort % python3 -m unittest discover -v
```
results:
```
Sorted list using mergesort_v1:  [1, 3, 5, 7, 9]
Sorted list using mergesort_v2:  [1, 3, 5, 7, 9]
Sorted list using mergesort_v1:  [1, 3, 5, 7, 9]
Sorted list using mergesort_v2:  [1, 3, 5, 7, 9]
test_decreasing_order (tests.test_merge_sort.TestMergeSortV1.test_decreasing_order) ... ok
test_empty_array (tests.test_merge_sort.TestMergeSortV1.test_empty_array) ... ok
test_increasing_order (tests.test_merge_sort.TestMergeSortV1.test_increasing_order) ... ok
test_random_order (tests.test_merge_sort.TestMergeSortV1.test_random_order) ... ok
test_single_element (tests.test_merge_sort.TestMergeSortV1.test_single_element) ... ok
test_decreasing_order (tests.test_merge_sort.TestMergeSortV2.test_decreasing_order) ... ok
test_empty_array (tests.test_merge_sort.TestMergeSortV2.test_empty_array) ... ok
test_increasing_order (tests.test_merge_sort.TestMergeSortV2.test_increasing_order) ... ok
test_random_order (tests.test_merge_sort.TestMergeSortV2.test_random_order) ... ok
test_single_element (tests.test_merge_sort.TestMergeSortV2.test_single_element) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.000s

OK```