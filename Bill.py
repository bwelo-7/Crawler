import pygame

from stuff import WIDTH, HEIGHT, RED
from Bob import spr_width, spr_height

b_pos_y = HEIGHT + 20
b_pos_x = WIDTH / 2

class Bill(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((spr_width, spr_height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT + 20

        self.rect.x = x
        self.rect.y = y
