# Depth-First Search (DFS) Algorithm

## Overview

The Depth-First Search (DFS) algorithm is a fundamental traversal algorithm used in graph theory to explore all the vertices and edges of a graph systematically. This implementation of the DFS algorithm not only traverses the graph but also calculates the sum of the distances (weights) of the edges from the starting vertex to the target vertex.

## Implementation Details

The DFS function is defined as follows:

```python
def dfs(graph, current_vertex, target_vertex, visited=None, distance=0):
```

- `graph`: The graph object on which the DFS algorithm will be executed. The graph should be an instance of a class that contains methods for checking vertex existence (`contains`), retrieving the edges from a vertex (`edges_from_vertex`), and managing vertices and edges.
- `current_vertex`: The vertex from which the search starts.
- `target_vertex`: The vertex that we want to reach.
- `visited`: A set to keep track of the visited vertices to avoid cycles. It is initialized to `None` and converted to an empty set on the first call.
- `distance`: Accumulates the sum of the distances (weights) of the edges as the algorithm traverses the graph. It starts with a default value of `0`.

## Function Behavior

- If `current_vertex` does not exist in the graph, the function returns `float('inf')`, indicating that the vertex is unreachable.
- If `current_vertex` is the `target_vertex`, it returns the current accumulated `distance`.
- For each unvisited neighbor connected to the `current_vertex`, it recursively calls itself with the neighbor as the new current_vertex.
- It keeps track of the minimum distance encountered during the traversal. If no path to the target is found, it returns `float('inf')`.

## Usage

To use the DFS algorithm, create an instance of the graph, add vertices and edges to the graph, and then call the dfs function with the desired starting and target vertices.

Example:
```python
g = Graph()
g.add_vertex(Vertex('A'))
g.add_vertex(Vertex('B'))
# ... additional vertices and edges ...
g.add_edge(Edge(Vertex('A'), Vertex('B'), 2))

distance = dfs(g, Vertex('A'), Vertex('B'))
print(f"Distance from 'A' to 'B': {distance}")
```
This will output the distance from vertex 'A' to vertex 'B' if there is a path. If the path does not exist, it will output infinity (`float('inf')`).

## Test Cases

The correctness of the `dfs` function can be verified by running predefined test cases that assert the function's behavior with various graph configurations and edge cases, such as paths that do not exist or starting from vertices that are not part of the graph.

