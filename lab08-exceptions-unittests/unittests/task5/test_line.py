from line import Point, Line
import unittest

class TestLine(unittest.TestCase):
    def setUp(self):
        # y = x
        self.line_yx = Line([Point(0 , 0), Point(7, 7)])
        # x = 1
        self.line_x = Line([Point(1 , -3), Point(1, 20)])

    # x = 1 - parallel to Oy
    def test_intersect1(self):
        self.assertEqual(None, self.line_x.intersect(
            Line([Point(3 , 1), Point(3, 4)])))

    def test_intersect2(self):
        self.assertEqual(self.line_x, self.line_x.intersect(
            Line([Point(1 , 1), Point(1, 4)])))

    def test_intersect3(self):
        point = self.line_x.intersect(self.line_yx)
        self.assertEqual((Point(1, 1).x, Point(1, 1).y), (point.x, point.y))

    # y = x - random function
    def test_intersect4(self):
        self.assertEqual(None, self.line_yx.intersect(
            Line([Point(-1 , -3), Point(3, 1)])))

    def test_intersect5(self):
        self.assertEqual(self.line_yx, self.line_yx.intersect(
            Line([Point(1 , 1), Point(-2, -2)])))
    
    def test_intersect6(self):
        point = self.line_yx.intersect(Line([Point(1 , -1), Point(-100, 100)]))
        self.assertEqual((Point(0, 0).x, Point(0, 0).y), (point.x, point.y))
        



if __name__ == '__main__':
    unittest.main()
