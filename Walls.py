import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        super().__init__()
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill((105, 95, 110))
        self.rect = self.image.get_rect(topleft=(x, y))

def load_map(filename, tile_size):
    walls = pygame.sprite.Group()
    with open(filename, 'r') as f:
        for row_index, line in enumerate(f):
            line = line.rstrip('\n')
            for col_index, char in enumerate(line):
                if char == '#':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    wall = Wall(x, y, tile_size)
                    walls.add(wall)
    return walls

def wall_collisions(sprite, walls):
    hits = pygame.sprite.spritecollide(sprite,walls, False)
    for wall in hits:
        if sprite.dx > 0:
            sprite.rect.right = wall.rect.left
            sprite.dx = 0
        elif sprite.dx < 0:
            sprite.rect.left  = wall.rect.right
            sprite.dx = 0

        if sprite.dy > 0:
            sprite.rect.bottom = wall.rect.top
            sprite.dy = 0
        if sprite.dy < 0:
            sprite.rect.top = wall.rect.bottom
