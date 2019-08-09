# The world class is the world space. It contains the player, enemies, physical objects, interactables, and so on

class world(object):
    def __init__(self, _rows, _cols, _x, _y, _size):
        self.rows = _rows
        self.cols = _cols
        self.x = _x
        self.y = _y
        self.size = _size
        self.xm = self.rows * self.size
        self.ym = self.cols * self.size

        self.spaces = []

        for row in range(self.rows):
            for col in range(self.cols):
                self.spaces.append([self.x + (row * self.size), self.y + (col * self.size)])

    def testPrint(self):
        for row in range(self.rows):
            for col in range(self.cols):
                print(self.spaces[row + (self.cols * col)], end="", flush=True)
            print()