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


def distance_btw(p1, p2):
    """Returns distance between points p1 and p2"""
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5 
    
