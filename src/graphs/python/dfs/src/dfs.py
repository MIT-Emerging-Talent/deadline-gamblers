from typing import Set, Optional
def dfs(graph, current_vertex, target_vertex,
        visited = None, distance: int = 0) -> float:
    """
    Perform a depth-first search (DFS) on a graph from a starting vertex to a target vertex,
    calculating the total distance of the discovered path. If the target vertex is not reachable,
    returns infinity.

    Parameters:
    - graph (Graph): The graph object containing vertices and edges.
    - current_vertex (Vertex): The starting vertex for the DFS.
    - target_vertex (Vertex): The vertex to find a path to.
    - visited (set, optional): Set of already visited vertices to avoid cycles. Defaults to None.
    - distance (int, optional): Accumulated distance from the starting vertex. Defaults to 0.

    Returns:
    int: The total distance of the path from current_vertex to target_vertex if such a path exists,
    otherwise float('inf').

    Assumptions:
    - The graph does not contain negative cycles.
    - Edge distances are positive integers.
    - Vertex equality is based on the value of the vertex.

    Doctests:
    >>> g = Graph()
    >>> for i in range(5): g.add_vertex(Vertex(i))
    >>> g.add_edge(Edge(Vertex(0), Vertex(1), 10))
    >>> g.add_edge(Edge(Vertex(0), Vertex(2), 5))
    >>> g.add_edge(Edge(Vertex(1), Vertex(2), 2))
    >>> g.add_edge(Edge(Vertex(1), Vertex(3), 1))
    >>> g.add_edge(Edge(Vertex(2), Vertex(3), 9))
    >>> g.add_edge(Edge(Vertex(3), Vertex(4), 3))
    >>> dfs(g, Vertex(0), Vertex(4))
    13
    >>> dfs(g, Vertex(0), Vertex(2))
    5
    >>> dfs(g, Vertex(4), Vertex(0))
    float('inf')
    """
    if visited is None:
        visited = set()
        
    if not graph.contains(current_vertex):
        return float('inf')

    visited.add(current_vertex)

    if current_vertex == target_vertex:
        return distance

    min_distance = float('inf')

    for edge in graph.edges_from_vertex(current_vertex):
        neighbor_vertex = edge.destination
        if neighbor_vertex not in visited:
            current_distance = dfs(graph, neighbor_vertex, target_vertex, visited, distance + edge.distance)
            if current_distance < min_distance:
                min_distance = current_distance
    return min_distance
