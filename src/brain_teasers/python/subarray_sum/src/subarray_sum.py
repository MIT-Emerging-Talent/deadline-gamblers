""" subarray_sum Module
This function provides is developed for calculating the sum of a sub-array from a given array.
It takes an array as input, makes a sub-array based on start and end indices, and calculates the sum of elements of the sub-array.
"""

def subarray_sum(arr, start_index, end_index):
    """
    Calculate the sum of a sub-array from a given array

    Parameters:
    - arr (list): Input list of integers.
    - start_index: Start index of the sub-array
    - end_index: End index of the sub-array

    Returns an integer representing sum of the sub-array
    """
    
    sub_array = arr[start_index:end_index]
    total = sum(sub_array)
    return total


# checks
# print(subarray_sum([0, 0, 0, 0], 0, 3) == 0)
# print(subarray_sum([10, 0, 0, 0], 1, 3) == 0)
# print(subarray_sum([10, 0, 0, 10], 0, 3) == 10)
# print(subarray_sum([10, 0, 0, 10], 0, 4) == 20)
# print(subarray_sum([10, 10, 10, 10], 1, 3) == 20)