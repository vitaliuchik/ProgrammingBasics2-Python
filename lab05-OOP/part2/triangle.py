class Triangle():
    """Represents point by three points"""

    def __init__(self, point1, point2, point3):
        """ Initializes triangle characteristics"""

        self.point1 = point1
        self.point2 = point2
        self.point3 = point3


    def lines(self):
        """ (Triangle) -> tuple
        Return tuple of lines' length"""

        line1 = ( (self.point1.x-self.point2.x)**2 \
                + (self.point1.y-self.point2.y)**2 )**0.5 
        line2 = ( (self.point2.x-self.point3.x)**2 \
                + (self.point2.y-self.point3.y)**2 )**0.5 
        line3 = ( (self.point1.x-self.point3.x)**2 \
                + (self.point1.y-self.point3.y)**2 )**0.5
        
        return (line1, line2, line3)

    
    def is_triangle(self):
        """ (Triangle) -> bool
        Determines if triangle exists"""

        line123 = self.lines()

        if (line123[0] + line123[1] > line123[2] and \
            line123[0] + line123[2] > line123[1] and \
            line123[2] + line123[1] > line123[0]):
            return True
        else:
            return False


    def perimeter(self):
        """ (Triangle) -> int
        Calculates perimeter"""

        line123 = self.lines()
        return sum(line123)


    def area(self):
        """ (Triangle) -> bool
        Calculates area"""

        line123 = self.lines()
        a = line123[0]
        b = line123[1]
        c = line123[2]

        S = 0.25 * ((a+b-c) * (a+c-b) * (b+c-a) * (a+b+c))**0.5
        return S

        


