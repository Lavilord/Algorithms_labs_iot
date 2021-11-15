import unittest
import binary_search_tree

class MyTestCase(unittest.TestCase):
    def test_insert_and_search(self):
        tree = binary_search_tree.Tree()
        tree.insert(5)
        tree.insert(6)
        tree.insert(3)
        tree.insert(7)
        self.assertEqual(True, tree.search(5))
        self.assertEqual(True, tree.search(7))
        self.assertEqual(True, tree.search(3))
        self.assertEqual(True, tree.search(6))

    def test_delete(self):
        tree = binary_search_tree.Tree()
        tree.insert(5)
        tree.insert(6)
        tree.insert(3)
        tree.insert(7)
        tree.delete(5)
        self.assertEqual(False, tree.search(5))

if __name__ == '__main__':
    unittest.main()
