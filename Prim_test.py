import unittest
import Prim

class MyTestCase(unittest.TestCase):
    def test_add_link(self):
        graph = Prim.Graph(3)
        graph.add_link(0, 1, -3)
        graph.add_link(0, 2, 2)
        graph.add_link(1, 2, 5)
        self.assertEqual(graph.graph, [[0, 1, -3], [0, 2, 2], [1, 2, 5]])

    def test_algorithm(self):
        graph = Prim.Graph(4)

        graph.add_link(0, 1, 5)
        graph.add_link(0, 4, 6)
        graph.add_link(1, 0, 5)
        graph.add_link(2, 4, 2)
        graph.add_link(2, 3, 1)
        graph.add_link(1, 2, 1)
        graph.add_link(3, 4, 3)
        graph.add_link(1, 3, 2)

        graph.Prim(0)

        self.assertEqual(graph.new_graph, [[0, 1, 5], [1, 2, 1], [2, 3, 1]])


if __name__ == '__main__':
    unittest.main()