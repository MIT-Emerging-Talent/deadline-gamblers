def dfs(graph, current_vertex, target_vertex, visited=None):
    if visited is None:
        visited = set()

    visited.add(current_vertex)

    if current_vertex == target_vertex:
        return 0

    for edge in graph.edges_from_vertex(current_vertex):
        neighbor_vertex = edge.destination
        if neighbor_vertex not in visited:
            distance_sum = dfs(graph, neighbor_vertex, target_vertex, visited)
            if distance_sum:
                return distance_sum + edge.distance

    return float('inf')