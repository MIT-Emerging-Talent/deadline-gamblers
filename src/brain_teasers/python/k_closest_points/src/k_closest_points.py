""" Module header: K_closest_points

This is designed for identification of the K closest points to the origin (0, 0) within a given list of points.
The function utilizes a helper function, `distance_function`, to calculate Euclidean distances.
"""

def k_closest_points(points: list[tuple[int, int]], k: int) -> list[tuple[int, int]]:
    """
    Finds the K closest points to the origin (0, 0) in a given list of points.

    Parameters:
    - points (list of tuples): A list containing points represented as tuples.
    - k (int): The number of closest points to return.

    Returns:
    list of tuples: The K closest points to the origin (0, 0).
    """

    def distance_function(point):
        """
        Helper function to calculate the Euclidean distance of a point from the origin (0, 0).

        Parameters:
        - point (tuple): A point represented as a tuple.
        """
        return ((point[0]-0)**2 + (point[1]-0)**2)**0.5
    
    return sorted(points, key=distance_function)[:k]


# checks
# print(k_closest_points([(-3, -4), (0, 0), (1, 1), (2, 2), (-1, -1), (-5, -6)], 3) == [(0, 0), (1, 1), (-1, -1)])
# print(k_closest_points([(1, 2), (3, 4), (-1, 0), (5, 6), (0, 0), (8, 8)], 2) == [(0, 0), (-1, 0)])
# print(k_closest_points([(-3, -4), (0, 0), (1, 1), (0, 0), (0, 0), (-5, -6)], 3) == [(0, 0), (0, 0), (0, 0)])