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

    def same_coordinates(self, rectangle):
        return (self.corner.x == rectangle.corner.x) and (self.corner.y == rectangle.corner.y)

    def get_all_points(self):
        """returns all points in rectangle object"""
        points = []
        a = list(range(self.corner.x, self.width + 1))
        b = list(range(self.corner.y, self.height + 1))

        for i in a:
            for j in b:
                p = (i, j)
                points.append(p)

        return points
            
        

    def collision(self, rectangle):
        """checks if the object collides with another rectangle"""
        if self.same_coordinates(rectangle):
            return True
        else:
            points = rectangle.get_all_points() #gets all points in d rectangle
            for point in points:
                if self.contains(point): #if point falls in d object, there's collision
                    return True
            return False
            
        
            
    
