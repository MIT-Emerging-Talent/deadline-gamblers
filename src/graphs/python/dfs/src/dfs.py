def dfs(graph, current_vertex, target_vertex, visited=None, distance=0):
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
