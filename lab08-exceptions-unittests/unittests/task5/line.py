class Point:
    """Represents point by two coordinates"""
    def __init__(self, x, y):
        # x, y - float coordinates
        self.x = x
        self.y = y


class Line:
    """Represents line by two points"""
    def __init__(self, points):
        # points - list of two Point objects
        self.points = points

    def intersect(self, other):
        """Returns point of intersection of two lines if exists,
returns None if lines are parallel and line if lines are the same"""
        x1 = self.points[0].x
        x2 = self.points[1].x
        x3 = other.points[0].x
        x4 = other.points[1].x
        y1 = self.points[0].y
        y2 = self.points[1].y
        y3 = other.points[0].y
        y4 = other.points[1].y

        if x1 != x2 and x3 != x4:
            k1 = (y1-y2)/(x1-x2)
            k2 = (y3-y4)/(x3-x4)

            if (y1-y2)==k1*(x1-x2) and \
                (y1-y3)==k1*(x1-x3) and (y1-y4)==k1*(x1-x4):
                return self
            # checks if line are parallel
            if k1 != k2:
                x = (x1*k1 - x3*k2 - y1 + y3)/(k1 - k2)
                y = k1*x - k1*x1 + y1
                return Point(x, y)

        elif x1 == x2 and x3 != x4:
            k = (y3-y4)/(x3-x4)
            x = x1
            y = k*x - k*x3 + y3
            return Point(x, y)

        elif x1 != x2 and x3 == x4:
            k = (y1-y2)/(x1-x2)
            x = x3
            y = k*x - k*x1 + y1
            return Point(x, y)

        else:
            if x1 == x3:
                return self




