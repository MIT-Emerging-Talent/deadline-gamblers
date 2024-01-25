# Member: Batool Alkaddah

def selectionsort_v1(arr: list()) -> list():
    """
    :param arr: list of unsorted numbers
    :return: list of sorted numbers
    """

    n = len(arr)

    #Base case
    if n <= 1:
        return arr

    # Not selection sort but it works :P
    # for i in range(n):
    #     min_val = min(arr)
    #     sorted_list.append(min_val)
    #     arr.remove(min_val)

    # Real selection sort
    for i in range(n):
        index= i
        for j in range(i+1, n):
            if arr[j] < arr[index]:
                index= j
        # Tuple unpacking to swap 2 var without 3rd one-
        # Swap min val to the current element inde, and vice versa
        arr[i], arr[index] = arr[index], arr[i]

    return arr

# print(selectionsort_v1([2, 5, 1, 4, 3]))