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


    def update(self, walls=None):
        # Move in small steps to prevent skipping walls
        steps = int(max(abs(self.dx), abs(self.dy), 1))
        for _ in range(steps):
            self.rect.x += self.dx / steps
            self.rect.y += self.dy / steps
            if walls and pygame.sprite.spritecollideany(self, walls):
                self.kill()
                break



        if self.rect.left > WIDTH or self.rect.right < 0 or self.rect.top > HEIGHT or self.rect.bottom < 0:
            self.kill()
