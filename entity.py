# All characters, npcs, and enemies inherit from this class so all generic methods should be contained here

# We import the bBox as entities are physical parts of the world
import bBox as bb

class Entity(bb.BoundingBox):

    def __init__(self, x, y, width, height, name):
        super().__init__(x, y, width, height)
        self._name = name
    
    # Use this to get an entities name which I reccomend to use as a unique ID and include actuall names in the actual entities
    @property
    def name(self):
        return self._name

    # This will be rarely used but it's there just incase you'd need to change an entity's id
    @name.setter
    def name(self, string):
        self._name = string