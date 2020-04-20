import unittest
import random
from intset import IntSet


class TestIntSet(unittest.TestCase):
    def setUp(self):
        random.seed(28)
        self.set0 = IntSet(0) # empty
        self.set5 = IntSet(5)
        self.set4 = IntSet(4)

    def testRandomSeed(self):
        self.assertEqual(str(self.set5), '14 95 16 69 76')
        self.assertEqual(str(self.set4), '91 22 28 16')

    def testTwoEmpty(self):
        result = self.set0.merge(self.set0)
        self.assertEqual(str(result), '')

    def testOneEmpty(self):
        result = self.set0.merge(self.set5)
        self.assertEqual(str(result), '1 4 9 5 1 6 6 9 7 6')

    def testTwoDifferent(self):
        result = self.set4.merge(self.set5)
        self.assertEqual(str(result), '1 0 5 1 1 7 4 4 8 5 7 6')


if __name__ == '__main__':
    unittest.main()