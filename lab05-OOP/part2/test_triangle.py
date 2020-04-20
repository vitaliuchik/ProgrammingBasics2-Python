import triangle
import point

if __name__ == '__main__':
    triangle1 = triangle.Triangle(point.Point(1, 1), \
                point.Point(3, 1), point.Point(2, 3))
    # b
    print(triangle1.is_triangle())
    # c
    print(triangle1.perimeter())
    # d
    print(triangle1.area())
