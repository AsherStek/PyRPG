# This is the default player class. This will be overhauledd as the framework progresses and new features are added

import random as rng
import entity

class Player(entity.Entity):

    def __init__(self, x, y, width, height, name, step, color, stats):
        super().__init__(x, y, width, height, name)
        self.activeMap = None
        self._step = step
        self._color = color
        self._stats = stats
    
    def placeInMap(self, newMap):
        self.activeMap = newMap
        self.x1 = self.activeMap.x
        self.y1 = self.activeMap.y

    # Getters
    @property
    def color(self):
        return self._color
    @property
    def step(self):
        return self._step
    @property 
    def stats(self):
        return self._stats 

    # Setter to change the player's primitive color
    @color.setter
    def color(self, string):
        self._color = string
    @step.setter
    def step(self, val):
        self._step = val
    @stats.setter
    def stats(self, list):
        self._stats = list

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

    def actions(self, choice):
        acts = {
            0 : self.attack,
            1 : self.defend,
            2 : self.skill,
            3 : self.flee
        }
        cmd = acts.get(choice)
        cmd()
    
    def attack(self, target):
        target.stats[0] -= rng.Random.randrange(0, target.stats[1]) - rng.Random.randrange(0, self.stats[3])

    def defend(self):
        return self.stats[1] * 1.5

    def skill(self, target, useSkill):
        pass

    def flee(self, target):
        if rng.Random.randrange(0, self.stats[5]) > target.stats[4]:
            return True
        else:
            return False

    # The movement functions
    def up(self):
        if (self.y1 - self.activeMap.size < 0):
            self.y1 = self.activeMap.y
        else:
            self.y1 -= self.activeMap.size
            self.y2 -= self.activeMap.size
    def down(self):
        if (self.y2 + self.activeMap.size > self.activeMap.ym):
            self.y2 = self.activeMap.ym
        else:
            self.y1 += self.activeMap.size
            self.y2 += self.activeMap.size
    def left(self):
        if (self.x1 - self.activeMap.size < 0):
            self.x1 = self.activeMap.x
        else:
            self.x1 -= self.activeMap.size
            self.x2 -= self.activeMap.size
    def right(self):
        if (self.x2 + self.activeMap.size > self.activeMap.xm):
            self.x2 = self.activeMap.xm
        else:
            self.x1 += self.activeMap.size
            self.x2 += self.activeMap.size