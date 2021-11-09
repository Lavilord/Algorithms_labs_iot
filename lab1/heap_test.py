import unittest
import heapsort


class TestAlgo(unittest.TestCase):

    def test_heap_sort(self):
        order = "asc"
        test_array = [1, 7, 3, 5, 2, -4, -5, 9, 23, 4, -6]
        heapsort.heapsort(test_array, order)
        test_answer = [-6,-5,-4,1,2,3,4,5,7,9,23]
        print(heapsort.swaps_counter)
        self.assertEqual(test_array, test_answer)

    def test_heap_sort_asc_asc(self):
        order = "asc"
        test_array = [-6,-5,-4,1,2,3,4,5,7,9,23]
        heapsort.heapsort(test_array, order)
        test_answer = [-6,-5,-4,1,2,3,4,5,7,9,23]
        print(heapsort.swaps_counter)
        self.assertEqual(test_array, test_answer)

    def test_heap_sort_asc_desc(self):
        order = "desc"
        test_array = [-6,-5,-4,1,2,3,4,5,7,9,23]
        heapsort.heapsort(test_array, order)
        test_answer = [23,9,7,5,4,3,2,1,-4,-5,-6]
        print(heapsort.swaps_counter)
        self.assertEqual(test_array, test_answer)

    def test_heap_sort_desc_asc(self):
        order = "asc"
        test_array = [23,9,7,5,4,3,2,1,-4,-5,-6]
        heapsort.heapsort(test_array, order)
        test_answer = [-6,-5,-4,1,2,3,4,5,7,9,23]
        print(heapsort.swaps_counter)
        self.assertEqual(test_array, test_answer)

    def test_heap_sort_desc_desc(self):
        order = "desc"
        test_array = [23,9,7,5,4,3,2,1,-4,-5,-6]
        heapsort.heapsort(test_array, order)
        test_answer = [23,9,7,5,4,3,2,1,-4,-5,-6]
        print(heapsort.swaps_counter)
        self.assertEqual(test_array, test_answer)

if __name__ == '__main__':
    unittest.main()