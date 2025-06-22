import pygame

from stuff import  RED
from Bob import Thing




class Bill(Thing):
    def __init__(self, x, y):
        Thing.__init__(self,x,y)
        self.image.fill(RED)
