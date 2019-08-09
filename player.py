# This is the default player class. This will be overhauledd as the framework progresses and new features are added

import entity

class Player(entity.Entity):
    def __init__(self, x, y, width, height, name, step, color):
        super().__init__(x, y, width, height, name)
        self._step = step
        self._color = color

    # Getters
    @property
    def color(self):
        return self._color
    @property
    def step(self):
        return self._step

    # Setter to change the player's primitive color
    @color.setter
    def color(self, string):
        self._color = string
    @step.setter
    def step(self, val):
        self._step = val

    # A basic movement switch case
    def move(self, dir):
        dirs = {
            'w' : self.up,
            's' : self.down,
            'a' : self.left,
            'd' : self.right
        }
        cmd = dirs.get(dir)
        cmd()
        print(f"X1: {self.x1} Y1: {self.y1} X2: {self.x2} Y2: {self.y2}")

    # The movement functions
    def up(self):
        self.y1 -= self.step
        self.y2 -= self.step
    def down(self):
        self.y1 += self.step
        self.y2 += self.step
    def left(self):
        self.x1 -= self.step
        self.x2 -= self.step
    def right(self):
        self.x1 += self.step
        self.x2 += self.step