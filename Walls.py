import pygame


from stuff import tile_size

game_map = [
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
"x------xxxx---------xxxx-----------xxxx----------x",
"x------xxxx---------xxxx-----------xxxx----------x",
"x------xxxx---------xxxx-----------xxxx--xxxx----x",
"x------xxxx---------xxxx-----------xxxx--xxxx----x",
"x----------------------------------------xxxx----x",
"x----------------------------------------xxxx----x",
"x------xxxx---------xxxx----------------xxxx-----x",
"x------xxxx---------xxxx----------------xxxx-----x",
"x------xxxx---------xxxx-------------------------x",
"xxxxxxxxxxxx--------xxxx-------------------------x",
"x----------x--------xxxx----xxxxxxxxxxxxxxxxx----x",
"x----------x----------------x---------------x----x",
"x----------x----------------x---------------x---x",
"x----------xxxxxxxxxxxxx----x---------------x---x",
"x---------------------------x---------------x---x",
"x---------------------------x---------------x---x",
"x----------xxxxxxxxxxxxx----x---------------x---x",
"x----------x----------------x---------------x---x",
"x----------x----------------x---------------x---x",
"x----------x--------xxxx----xxxxxxxxxxxxxxxxx---x",
"xxxxxxxxxxxx--------xxxx------------------------x",
"x------xxxx---------xxxx------------------------x",
"x------xxxx---------xxxx----------------xxxx----x",
"x------xxxx---------xxxx----------------xxxx----x",
"x----------------------------------------xxxx----x",
"x----------------------------------------xxxx----x",
"x------xxxx---------xxxx-----------xxxx--xxxx----x",
"x------xxxx---------xxxx-----------xxxx--xxxx----x",
"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
]

# Convert from strings to lists:
game_map = [list(row) for row in game_map]



class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        super().__init__()
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill((105, 95, 110))
        self.rect = self.image.get_rect(topleft=(x, y))


class Loadmap:
    def __init__(self, game_map, tile_size):
            self.walls = pygame.sprite.Group()


            for row_index, row in enumerate(game_map):
                for col_index, tile in enumerate(row):
                    if tile == 'x':
                        pixel_y = row_index * tile_size
                        pixel_x = col_index * tile_size
                        wall = Wall(pixel_x, pixel_y, tile_size)
                        self.walls.add(wall)




def wall_collisions(sprite, walls):
    sprite.rect.x += int(round(sprite.dx))
    hits = pygame.sprite.spritecollide(sprite, walls, False)
    for wall in hits:
        if sprite.dx > 0:
            sprite.rect.right = wall.rect.left
        elif sprite.dx < 0:
            sprite.rect.left = wall.rect.right
        sprite.dx = 0


    sprite.rect.y += int(round(sprite.dy))
    hits = pygame.sprite.spritecollide(sprite, walls, False)
    for wall in hits:
        if sprite.dy > 0:
            sprite.rect.bottom = wall.rect.top
        elif sprite.dy < 0:
            sprite.rect.top = wall.rect.bottom
        sprite.dy = 0




