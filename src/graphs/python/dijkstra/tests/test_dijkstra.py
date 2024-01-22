import unittest
import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from graph import Vertex, Edge, Graph
from dijkstra import dijkstra


class TestDijkstra(unittest.TestCase):
    def test_dijkstra_str_vertices_negative(self):
        graph = Graph()

        for vertex_label in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
            graph.add_vertex(Vertex(vertex_label))

        graph.add_edge(Edge(Vertex("A"), Vertex("D"), 2))
        graph.add_edge(Edge(Vertex("A"), Vertex("G"), 3))
        graph.add_edge(Edge(Vertex("A"), Vertex("B"), 1))
        graph.add_edge(Edge(Vertex("B"), Vertex("E"), 6))
        graph.add_edge(Edge(Vertex("B"), Vertex("F"), 7))
        graph.add_edge(Edge(Vertex("F"), Vertex("D"), 10))
        graph.add_edge(Edge(Vertex("F"), Vertex("C"), 12))
        graph.add_edge(Edge(Vertex("E"), Vertex("G"), 9))

        self.assertEqual(dijkstra(graph, Vertex("A"), Vertex("C")), 20)
        self.assertEqual(dijkstra(graph, Vertex("A"), Vertex("F")), 8)
        self.assertEqual(dijkstra(graph, Vertex("B"), Vertex("G")), 15)
        self.assertEqual(dijkstra(graph, Vertex("E"), Vertex("A")), float('inf'))
        self.assertEqual(dijkstra(graph, Vertex("C"), Vertex("D")), float('inf'))

    def test_dijkstra_int_vertices_positive(self):
        graph = Graph()

        for vertex_label in [0, 1, 2, 3, 4]:
            graph.add_vertex(Vertex(vertex_label))

        graph.add_edge(Edge(Vertex(0), Vertex(1), 1))
        graph.add_edge(Edge(Vertex(0), Vertex(4), 1))
        graph.add_edge(Edge(Vertex(1), Vertex(0), 1))
        graph.add_edge(Edge(Vertex(1), Vertex(3), 1))
        graph.add_edge(Edge(Vertex(1), Vertex(4), 1))
        graph.add_edge(Edge(Vertex(1), Vertex(2), 1))
        graph.add_edge(Edge(Vertex(2), Vertex(3), 1))
        graph.add_edge(Edge(Vertex(2), Vertex(1), 1))
        graph.add_edge(Edge(Vertex(3), Vertex(1), 1))
        graph.add_edge(Edge(Vertex(3), Vertex(2), 1))
        graph.add_edge(Edge(Vertex(3), Vertex(4), 1))

        # Add the missing vertex
        graph.add_vertex(Vertex(2))

        self.assertEqual(dijkstra(graph, Vertex(0), Vertex(2)), 2)
        self.assertEqual(dijkstra(graph, Vertex(1), Vertex(2)), 1)
        self.assertEqual(dijkstra(graph, Vertex(2), Vertex(2)), 0)
        self.assertEqual(dijkstra(graph, Vertex(3), Vertex(2)), 1)
        self.assertEqual(dijkstra(graph, Vertex(2), Vertex(4)), 2)

    def test_dijkstra_int_vertices_negative(self):
        graph = Graph()

        for vertex_label in [0, 1, 2, 3, 4]:
            graph.add_vertex(Vertex(vertex_label))

        graph.add_edge(Edge(Vertex(1), Vertex(2), 1))
        graph.add_edge(Edge(Vertex(1), Vertex(4), 1))
        graph.add_edge(Edge(Vertex(3), Vertex(4), 1))
        graph.add_edge(Edge(Vertex(4), Vertex(2), 1))

        # Add the missing vertices
        graph.add_vertex(Vertex(5))
        graph.add_vertex(Vertex(0))

        self.assertEqual(dijkstra(graph, Vertex(5), Vertex(0)), float('inf'))
        self.assertEqual(dijkstra(graph, Vertex(1), Vertex(5)), float('inf'))


if __name__ == "__main__":
    unittest.main()
