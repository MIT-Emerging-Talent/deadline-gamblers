"""
Module: quick_sort
This module provides two versions of the quicksort algorithm.
Each version has a slightly different approach to sorting an array of numbers.
"""


def quicksort_v1(array: list) -> list:
    """
    Sorts an array using the quicksort algorithm (Version 1).

    This function implements the quicksort algorithm to sort an array of
    numbers in ascending order. It uses a recursive approach where the
    pivot is chosen as the last element in the array.

    Parameters:
    array (list): The list of numbers to be sorted.

    Returns:
    list: A new list containing the sorted elements.

    Assumptions:
    - The input array contains numeric values only.

    Doctests:
    >>> quicksort_v1([])
    []
    >>> quicksort_v1([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    >>> quicksort_v1([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """
    if len(array) <= 1:
        return array

    pivot = array[-1]
    left = [x for x in array if x < pivot]
    right = [x for x in array if x > pivot]

    return quicksort_v1(left) + [pivot] + quicksort_v1(right)


def quicksort_v2(array: list) -> list:
    """
    Sorts an array using the quicksort algorithm (Version 2).

    This function implements the quicksort algorithm to sort an array of
    numbers in ascending order. It uses a recursive approach with a different
    strategy for choosing the pivot and partitioning the array compared to
    version 1.

    Parameters:
    array (list): The list of numbers to be sorted.

    Returns:
    list: A new list containing the sorted elements.

    Assumptions:
    - The input array contains numeric values only.

    Doctests:
    >>> quicksort_v2([])
    []
    >>> quicksort_v2([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    >>> quicksort_v2([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """

    def partition_sort(arr, low, high):
        pivot, i = arr[high], low
        for j in range(low, high):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition_sort(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)

    quick_sort_helper(array, 0, len(array) - 1)
    return array
