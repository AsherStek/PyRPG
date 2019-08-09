# This class is used to give any ingame objects a "physical" shape

class BoundingBox(object):

    # Initalize the space that the object in
    def __init__(self, x, y, width, height):
        self._width = width
        self._height = height
        self._x1 = x
        self._y1 = y
        self._x2 = x + width
        self._y2 = y + height

    # Getters to pull the bounds
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @property
    def x1(self):
        return self._x1
    @property
    def y1(self):
        return self._y1
    @property
    def x2(self):
        return self._x2
    @property
    def y2(self):
        return self._y2

    # Setters to change the bounds
    @width.setter
    def width(self, val):
        self._width = val
    @height.setter
    def height(self, val):
        self._height = val
    @x1.setter
    def x1(self, val):
        self._x1 = val
    @y1.setter
    def y1(self, val):
        self._y1 = val
    @x2.setter
    def x2(self, val):
        self._x2 = val
    @y2.setter
    def y2(self, val):
        self._y2 = val
    