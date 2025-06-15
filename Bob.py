import pygame

from Crawler import GREEN, WIDTH, HEIGHT, x, y, keys, speed, ax, ay


class Bob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT +20

        self.rect.x = x
        self.rect.y = y

    #def constraints(player):
        #if self.rect.x >

    def update(self):
        if keys[pygame.K_a]:
            self.rect.x -= (speed * ax)
        if keys[pygame.K_d]:
            self.rect.x += (speed * ax)
        if keys[pygame.K_s]:
            self.rect.y += ay
        if keys[pygame.K_w]:
            self.rect.y -= ay
