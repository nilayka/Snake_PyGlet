from random import randint
from Color import Color

class Food:
    def __init__(self, location=None, color=Color.RED, cell_size=10):
        self.x, self.y = location
        self.color = color
        self.cell_size = cell_size

    def set_location(self, location):
        self.x, self.y = location