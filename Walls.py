import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        super().__init__()
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill((100, 100, 100))  # gray color for walls
        self.rect = self.image.get_rect(topleft=(x, y))
