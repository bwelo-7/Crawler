import pygame

from stuff import GREEN, WIDTH, HEIGHT
x = 325
y = 610
speed = 2
ax = 10
ay = 10


class Bob(pygame.sprite.Sprite):
    def __init__(self, x,y):
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

    def update(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= (speed * ax)
        if keys[pygame.K_d]:
            self.rect.x += (speed * ax)
        if keys[pygame.K_s]:
            self.rect.y += ay
        if keys[pygame.K_w]:
            self.rect.y -= ay
