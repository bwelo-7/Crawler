import pygame
from Bob import Thing
from stuff import ORANGE, proj_width, proj_height, ax, ay, speed

class Fireball(Thing):
    def __init__(self, x, y):
        Thing.__init__(self,x,y)
        self.image = pygame.Surface((proj_width, proj_height))
        self.image.fill(ORANGE)


    def update(self, keys):
        self.shoot(keys)

    def shoot(self, keys):
        if keys[pygame.K_SPACE]:
            draw = True
            self.dy + ay
            print(self.rect.y)

        self.rect.y += self.dy