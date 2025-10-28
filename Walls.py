import pygame


map =[["x","x","x","x","x","x","x","x","x"],
      ["x","-","-","-","-","-","-","-","x"],
      ["x","-","-","-","-","-","-","-","x"],
      ["x","-","-","-","-","-","-","-","x"],
      ["x","-","-","-","-","-","-","-","x"],
      ["x","-","-","-","-","-","-","-","x"],
      ["x","-","-","-","-","-","-","-","x"],
      ["x","x","x","x","x","x","x","x","x"]]


for y, row in enumerate(map):
    print ("\n")
    for x,tile in enumerate(map):
        print(x)


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
