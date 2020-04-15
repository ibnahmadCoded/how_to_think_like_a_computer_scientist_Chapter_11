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

    def slope_from_origin(self):
        """Returns slope of line the point 'self' forms with the origin (0,0)"""
        return self.y / self.x
