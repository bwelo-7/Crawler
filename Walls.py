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