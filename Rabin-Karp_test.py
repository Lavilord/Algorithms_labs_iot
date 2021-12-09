import unittest
import Rabin_Karp

class TestRabinKarp(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Rabin_Karp.search("vev", "hevevhjbevbwjwvbvne", 101), [2])


if __name__ == '__main__':
    unittest.main()
