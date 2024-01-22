import heapq

def dijkstra(graph, start, end):
  queue = []
  heapq.heappush(queue, (0, start))
  distances = {vertex: float('infinity') for vertex in graph.vertices()}
  distances[start] = 0
  paths = {vertex: None for vertex in graph.vertices()}
  paths[start] = []

  while queue:
      current_distance, current_vertex = heapq.heappop(queue)

      if distances[current_vertex] < current_distance:
          continue

      for edge in graph.edges_from_vertex(current_vertex):
          adjacent = edge.destination
          weight = edge.distance
          distance = current_distance + weight

          if distance < distances[adjacent]:
              distances[adjacent] = distance
              paths[adjacent] = paths[current_vertex] + [current_vertex]
              heapq.heappush(queue, (distance, adjacent))

  return distances[end]
