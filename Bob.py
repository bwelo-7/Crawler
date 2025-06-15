import pygame

from stuff import GREEN, WIDTH, HEIGHT
from utils import bracket

speed = 2
ax = 1
ay = 1


class Bob(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT + 20
        self.fx = 0.8
        self.fy = 0.8
        self.dx = 0
        self.dy = 0
        self.rect.x = x
        self.rect.y = y

    def update(self, keys):
        self.dynamic_movement(keys)
        # self.linear_movement(keys)

    def dynamic_movement(self, keys):
        if keys[pygame.K_a]:
            self.dx -= ax
        elif keys[pygame.K_d]:
            self.dx += ax
        else:
            self.dx *= self.fx

        if keys[pygame.K_w]:
            self.dy -= ay
        elif keys[pygame.K_s]:
            self.dy += ay
        else:
            self.dy *= self.fx

        self.rect.x += self.dx
        self.rect.y += self.dy
        if 0.1 > self.dx > -0.1:
            self.dx = 0
        if 0.1 > self.dy > -0.1:
            self.dy = 0

        self.dx = bracket(self.dx, -10, 10)
        self.dy =bracket(self.dy, -10, 10)
        print("dx:", self.dx, "x: ", self.rect.x, "dy:", self.dy, "y: ", self.rect.y)
