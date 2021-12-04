import unittest
import IJones


class MyTestCase(unittest.TestCase):
    def test_1_plate(self):
        self.assertEqual(IJones.ijones(1, 1, "a"), 1)

    def test_file_1(self):
        input_file_params = IJones.read_file("in.txt")
        self.assertEqual(IJones.ijones(*input_file_params), 5)

    def test_file_2(self):
        input_file_params = IJones.read_file("in1.txt")
        self.assertEqual(IJones.ijones(*input_file_params), 2)

    def test_file_3(self):
        input_file_params = IJones.read_file("in2.txt")
        self.assertEqual(IJones.ijones(*input_file_params), 201684)

if __name__ == '__main__':
    unittest.main()
