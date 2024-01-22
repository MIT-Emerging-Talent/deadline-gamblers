# K Closest Points to (0, 0)

This `python` function finds the K closest points to (0, 0) in a given list of points.

```
# function: 
k_closest_points(points, k)

# parameters:
points: a list of points
k: number of closest points to return
```

A helper function is defined to calculate the distance between of each point from (0, 0).
The list of points is then sorted based on this helper function and the k points with minimum distance are returned.

```
k_closest_points([(-3, -4), (0, 0), (1, 1), (2, 2), (-1, -1), (-5, -6)], 3)
output: [(0, 0), (1, 1), (-1, -1)]

k_closest_points([(1, 2), (3, 4), (-1, 0), (5, 6), (0, 0), (8, 8)], 2)
output: [(0, 0), (-1, 0)]

k_closest_points([(-3, -4), (0, 0), (1, 1), (0, 0), (0, 0), (-5, -6)], 3)
output: [(0, 0), (0, 0), (0, 0)]

```

## Test Code Implementation

Run below code in `k_closest_points` directory.

```bash
python -m unittest discover -v
```

## Summary

This `k_closest_points` functiion identifies the K closest points to the origin (0, 0) from a given list of points. The implementation includes a helper function to calculate distances. Furthermore, examples are provided for usage along with a test code for validation.
