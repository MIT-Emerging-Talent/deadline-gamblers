def merge(left, right):
    """
    Merge two sorted lists into a single sorted list.

    Parameters:
    - left : The first sorted list.
    - right : The second sorted list.

    Returns:
    - list: The merged list, sorted in ascending order.
    """
    merged_list = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

    merged_list.extend(left[left_index:])
    merged_list.extend(right[right_index:])

    return merged_list


def mergesort_v1(array):
    """
    Sorts an array recursivly using the merge sort algorithm.

    Parameters:
        array : The array to be sorted.

    Returns:
        list: The sorted array.
    """
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left_half = mergesort_v1(array[:mid])
    right_half = mergesort_v1(array[mid:])

    return merge(left_half, right_half)


def mergesort_v2(array):
    """
    Sorts an array using the merge sort algorithm.

    Parameters:
        array : The array to be sorted.

    Returns:
        list: The sorted array.
    """
    def _merge_sort(items, start, end):
        if end - start > 1:
            mid = (start + end) // 2
            _merge_sort(items, start, mid)
            _merge_sort(items, mid, end)
            left, right = items[start:mid], items[mid:end]
            merged, left_index, right_index = [], 0, 0
            while left_index < len(left) and right_index < len(right):
                if left[left_index] < right[right_index]:
                    merged.append(left[left_index])
                    left_index += 1
                else:
                    merged.append(right[right_index])
                    right_index += 1
            merged.extend(left[left_index:])
            merged.extend(right[right_index:])
            items[start:end] = merged
        return items

    return _merge_sort(array, 0, len(array))
