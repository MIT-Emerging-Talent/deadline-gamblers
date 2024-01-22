def array_product(arr):
    """
    Calculate the product of all elements in an input array, excluding the element at each index.

    Parameters:
    - arr (list): Input list of integers.

    Returns:
    - list: A new list where each element represents the product of all elements in the input
            array except the one at the corresponding index.
    """
    if len(arr) == 1:
        return arr
    
    arr_new = []
    for i in range(len(arr)):
        arr_copy = arr[:i] + arr[i+1:]
        # print(arr_copy)
        product = 1
        for num in arr_copy:
            product *= num
        # print(product)
        arr_new.append(product)
        # print(arr_new)
    
    return arr_new

# checks
# print(product_of_array_except_self([1, 2, 3, 4, 5, 6, 7]) == [5040, 2520, 1680, 1260, 1008, 840, 720])
# print(product_of_array_except_self([1, 2, 3, 4, 5, 6, 0]) == [0, 0, 0, 0, 0, 0, 720])
# print(product_of_array_except_self([0, 2, 3, 4, 5, 6, 7]) == [5040, 0, 0, 0, 0, 0, 0])
# print(product_of_array_except_self([]) == [])
# print(product_of_array_except_self([1]) == [1])
# print(product_of_array_except_self([0]) == [0])