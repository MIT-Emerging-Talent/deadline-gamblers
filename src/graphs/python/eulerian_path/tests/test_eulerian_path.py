"""
Eulerian path is a trail in a finite graph that visits every edge exactly once. Vertices can be revisited.

There are two algorithms used to construct eulerain paths in graphs:
1. Fleury's algorithm
2. Hierholzer's algorithm
"""

import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from eulerian_path import fleury


G = {0: [2, 2, 3], 1: [2, 2, 3], 2: [0, 0, 1, 1, 3], 3: [0, 1, 2]}
assert not fleury(G)

G = {
    0: [1, 4, 6, 8],
    1: [0, 2, 3, 8],
    2: [1, 3],
    3: [1, 2, 4, 5],
    4: [0, 3],
    5: [3, 6],
    6: [0, 5, 7, 8],
    7: [6, 8],
    8: [0, 1, 6, 7],
}
result = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 1),
    (1, 8),
    (8, 0),
    (0, 4),
    (4, 3),
    (3, 5),
    (5, 6),
    (6, 8),
    (8, 7),
    (7, 6),
    (6, 0),
]

assert fleury(G) == result

G = {1: [2, 3, 4, 4], 2: [1, 3, 3, 4], 3: [1, 2, 2, 4], 4: [1, 1, 2, 3]}
result = [(1, 2), (2, 3), (3, 1), (1, 4), (4, 3), (3, 2), (2, 4), (4, 1)]

assert fleury(G) == result

G = {1: [2, 3], 2: [1, 3, 4], 3: [1, 2, 4], 4: [2, 3]}
result = [(2, 1), (1, 3), (3, 2), (2, 4), (4, 3)]

assert fleury(G) == result
