import unittest

import square_preceding


class TestPoint(unittest.TestCase):
    def test_three(self):
        l = [1, 2, 3]
        square_preceding.square_preceding(l)
        self.assertEqual(l, [0, 1, 4])

    def test_empty(self):
        l = []
        square_preceding.square_preceding(l)
        self.assertEqual(l, [])

    def test_one(self):
        l = [1]
        square_preceding.square_preceding(l)
        self.assertEqual(l, [0])

    def test_two(self):
        l = [1, 2]
        square_preceding.square_preceding(l)
        self.assertEqual(l, [0, 1])



if __name__ == '__main__':
    unittest.main()




