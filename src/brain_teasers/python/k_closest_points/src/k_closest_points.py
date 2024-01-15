def k_closest_points(points, k):
    def distance_function(point):
        return ((point[0]-0)**2 + (point[1]-0)**2)**0.5
    
    return sorted(points, key=distance_function)[:k]


# checks
# print(k_closest_points([(-3, -4), (0, 0), (1, 1), (2, 2), (-1, -1), (-5, -6)], 3) == [(0, 0), (1, 1), (-1, -1)])
# print(k_closest_points([(1, 2), (3, 4), (-1, 0), (5, 6), (0, 0), (8, 8)], 2) == [(0, 0), (-1, 0)])
# print(k_closest_points([(-3, -4), (0, 0), (1, 1), (0, 0), (0, 0), (-5, -6)], 3) == [(0, 0), (0, 0), (0, 0)])