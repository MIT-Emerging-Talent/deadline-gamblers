import random

def randomize_array(original_array):
    """
    Randomizes the order of elements in the given array.

    Parameters:
        original_array (list): The original array to be randomized.
        
    Returns:
        list: A new array with the elements of the original array in random order.
    """
    randomized_array = original_array.copy()
    random.shuffle(randomized_array)
    return randomized_array