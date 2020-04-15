from study import *

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width,
                                      self.height)

    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        """Returns area of rectangle object"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of rectangle object"""
        return 2 * (self.width + self.height)

    def flip(self):
        """swaps the height and the width of the object"""
        w = self.width
        self.width = self.height
        self.height = w

    def contains(self, point):
        a = point.x >= self.corner.x and point.x < self.width
        b = point.y >= self.corner.y and point.y < self.height

        return a and b
        #return point.x in range(self.corner.x, self.width) and point.y in range(self.corner.y, self.height)
    
