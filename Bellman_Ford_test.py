import unittest
import Bellman_Ford

class MyTestCase(unittest.TestCase):
    def test_add_link(self):
        graph = Bellman_Ford.Graph(5)
        graph.add_link(0, 1, -3)
        graph.add_link(0, 2, 2)
        graph.add_link(1, 2, 5)
        self.assertEqual(graph.graph, [[0, 1, -3], [0, 2, 2], [1, 2, 5]])

    def test_algorithm(self):
        graph = Bellman_Ford.Graph(5)
        graph.add_link(0, 1, -2)
        graph.add_link(0, 2, 3)
        graph.add_link(1, 2, 7)
        graph.add_link(1, 3, 8)
        graph.add_link(1, 4, 3)
        graph.add_link(3, 2, 6)
        graph.add_link(3, 1, 9)
        graph.add_link(4, 3, -5)

        graph.Bellman_Ford(0)
        self.assertEqual(graph.dist, [0, -2, 2, -4, 1])

    def test_negative_cyckle_detection(self):
        graph = Bellman_Ford.Graph(5)
        graph.add_link(0, 1, -2)
        graph.add_link(0, 2, -3)
        graph.add_link(1, 2, -7)
        graph.add_link(1, 3, -8)
        graph.add_link(1, 4, -3)
        graph.add_link(3, 2, -6)
        graph.add_link(3, 1, -9)
        graph.add_link(4, 3, -5)

        graph.Bellman_Ford(0)
        self.assertEqual(graph.dist, [None])


if __name__ == '__main__':
    unittest.main()

