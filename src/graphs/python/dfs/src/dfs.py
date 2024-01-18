def dfs(graph, current_vertex, target_vertex, visited=None):
    if visited is None:
        visited = set()

    visited.add(current_vertex)

    if current_vertex == target_vertex:
        return True

    for edge in graph.edges_from_vertex(current_vertex):
        neighbor_vertex = edge.destination
        if neighbor_vertex not in visited:
            if dfs(graph, neighbor_vertex, target_vertex, visited):
                return True

    return False