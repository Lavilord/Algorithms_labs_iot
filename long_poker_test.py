import unittest
import long_poker


class MyTestCase(unittest.TestCase):
    def test_something(self):
        poker = long_poker.Poker()
        text_file = open("test_poker_in.txt", "r")
        poker_In_list = text_file.read().split(" ")
        poker_In_list = list(map(float, poker_In_list))
        poker_In_list = list(map(int, poker_In_list))
        text_file.close()
        poker.card_list = poker.sort_and_unify(poker_In_list)
        poker.search_longest_combination()
        self.assertEqual(poker.max_combination, 13)


if __name__ == '__main__':
    unittest.main()
