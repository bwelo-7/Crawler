import pygame
from Bob import Thing
from stuff import ORANGE, proj_width, proj_height, ax, ay, speed, WIDTH, HEIGHT

class Fireball(Thing):
    def __init__(self, x, y, dx = 0, dy = 10):
        super().__init__(x, y)
        self.image = pygame.Surface((proj_width, proj_height))
        self.image.fill(ORANGE)
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = dx
        self.dy = dy

    def update(self,keys, joystick):
        self.rect.x += int(self.dx)
        self.rect.y += int(self.dy)


        if self.rect.left > WIDTH or self.rect.right < 0 or self.rect.top > HEIGHT or self.rect.bottom < 0:
            self.kill()
