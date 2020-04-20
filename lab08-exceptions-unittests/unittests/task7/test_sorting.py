import unittest
from is_sorted import is_sorted

class TestSorting(unittest.TestCase):
    def test_sorting1(self):
        self.assertTrue(is_sorted([1, 2, 3]))

    def test_sorting2(self):
        self.assertTrue(is_sorted([1, 1, 2, 3]))

    def test_sorting3(self):
        self.assertTrue(is_sorted([]))

    def test_sorting4(self):
        self.assertTrue(is_sorted([4]))

    def test_sorting5(self):
        self.assertFalse(is_sorted([3, 2, 1]))

    def test_sorting6(self):
        self.assertFalse(is_sorted([3, 2, 3]))


if __name__ == '__main__':
    unittest.main()

        