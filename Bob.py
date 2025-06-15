import pygame

from stuff import GREEN, WIDTH, HEIGHT

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

    def linear_movement(self, keys):
        if keys[pygame.K_a]:
            self.rect.x -= (speed * ax)
        if keys[pygame.K_d]:
            self.rect.x += (speed * ax)
        if keys[pygame.K_s]:
            self.rect.y += ay
        if keys[pygame.K_w]:
            self.rect.y -= ay

    def dynamic_movement(self, keys):
        if keys[pygame.K_a]:
            self.dx -= ax
        if keys[pygame.K_d]:
            self.dx += ax
        if keys[pygame.K_w]:
            self.dy -= ax
        if keys[pygame.K_s]:
            self.dy += ax





        self.rect.x += self.dx
        self.rect.y += self.dy

        print("ax: ",ax, "dx:",self.dx, "x: ",self.rect.x)
