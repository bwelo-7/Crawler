from Bob     import Thing
import pygame
from stuff import RED

class Bill(Thing):
    def __init__(self, x, y):
        super().__init__(x, y, 3)
        self.image.fill(RED)

    def update(self, *args):
        pass