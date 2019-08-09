# This is the enemy class. For now it will be a single type of enemy but in future revisions I want to make it so that the enemy is dynamically created based of of a name in a table of enemies

import random as rng

import entity

class Enemy(entity.Entity):

    def __init__(self, x, y, width, height, name, _color, _stats):
        super().__init__(x, y, width, height, name)
        self.color = _color
        self.stats = _stats # (hp, def, sp, atk, spd, luk)

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
