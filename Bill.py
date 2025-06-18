import pygame

from stuff import WIDTH, HEIGHT, RED
from Bob import spr_width, spr_height, Thing


# b_pos_y = HEIGHT + 20
# b_pos_x = WIDTH / 2

class Bill(Thing):
    def __init__(self, x, y):
        Thing.__init__(self,x,y)
        self.image.fill(RED)
