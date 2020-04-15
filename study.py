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

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __rmul__(self, other):
        return Point(other * self.x, other.self.y)

    def reverse(self):
        (self.x, self.y) = (self.y, self.x)

def front_and_back(front):
    import copy
    back = copy.copy(front)
    back.reverse()
    print(str(front) + str(back))


