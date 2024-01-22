# Insertion Sort Algorithm

This Python module provides an implementation of the Insertion Sort algorithm. It sorts a list of comparable elements in ascending order.

## Installation

No installation is required. Simply include the `sort.py` file in your project and import the `insertionsort_v1` function.

## Implementation Details

The function iterates through the input list, maintaining a sorted section at the beginning. It compares each element with the elements in the sorted section and inserts it into its correct position.
        key: The current element being compared and inserted.
        j: The index of the last element in the sorted section.
The while loop shifts elements in the sorted section to make space for the key, and the final position of the key is determined when the loop exits.    

## Example

    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = insertionsort_v1(arr)
    print(sorted_arr)
This will output:
    [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

