class Point():
    """Point class represents and manipulates x,y coords. """

    def __init__(self, x = 0, y = 0):
        """Create a new point at the origin """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """Compute my distance from the origin"""
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        """prints the point coord"""
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """Return the midpoint of self and target point"""
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

    def distance_to(self, target):
        """Returns distance between self and target point"""
        return ((target.x - self.x) ** 2 + (target.y - self.y) ** 2) ** 0.5

    def reflect_x(self):
        """
            returns a new Point, one which is the reflection of the point
            about the x-axis. For example, Point(3, 5).reflect_x() is (3, -5)
        """
        a = self.x
        b = self.y * -1
        return Point(a, b)

    def slope_from_target(self, target):
        """Returns slope of line the point 'self' forms with target)"""
        return (target.y - self.y) / (target.x - self.x)

    def get_line_to(self, target):
        """
            returns coefficients a and b in the line equation (y = mx + b) that
            points self and target form with each other
        """
        m = self.slope_from_target(target) #calculate the slope
        b = -m * self.x + self.y          #calculate constant b
        return int(m), int(b)

def get_circle_midpoint(p1, p2, p3, p4):
    """calculates circle's midpoint given four points"""
    line_1 = p1.get_line_to(p2)
    line_2 = p3.get_line_to(p4)
    #get line_1 constants
    m1 = line_1[0]
    b1 = line_1[1]
    #get line_2 constants
    m2 = line_2[0]
    b2 = line_2[1]

    x = (b2 - b1) / (m1 - m2)
    y = (m1 * x) + b1

    #return x, y
    return "Midpoint of circle is coordinate: ({0}, {1})".format(x, y)
    
