import pygame
import math
from Bill import Bill
from Bob import Bob
from Controller import KeyboardController
from Projectiles import Fireball
#from Controller import con_movement
from stuff import BLACK, WIDTH, HEIGHT, tile_size
from Walls import *



FPS = 30
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Crawler')
clock = pygame.time.Clock()


controller = None

if pygame.joystick.get_count() == 0:
    controller = KeyboardController()
else:
    controller = pygame.joystick.Joystick(0)
    controller.init()

fireballs = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()

all_sprites.add(Bob(60, 70))

all_sprites.add(Bill(300, 300))



Fireball_cooldown = 800
Fireball_cooldown_2 = 400
fireball_speed = 10
last_fireball_time = 0


map_loader = Loadmap(game_map, tile_size)
walls = map_loader.walls



# walls = load_map('map.txt', tile_size)

#game loop
running = True
while running:
    #keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
            #check for closing the window
            if event.type == pygame.QUIT:
                running = False


    keys = pygame.key.get_pressed()
    current_time = pygame.time.get_ticks()

    R2_axis = controller.get_axis(5)
    right_x = controller.get_axis(2)
    right_y = controller.get_axis(3)
    magnitude = math.hypot(right_x, right_y)

    # Update
    if R2_axis > -0.5 and magnitude > 0.1:
        dx = (right_x / magnitude) * fireball_speed
        dy = (right_y / magnitude) * fireball_speed

        for sprite in all_sprites:
            if isinstance(sprite, Bob):
                if current_time - last_fireball_time > Fireball_cooldown:
                    fireball = Fireball(sprite.rect.centerx, sprite.rect.centery, dx =dx, dy =dy )
                    all_sprites.add(fireball)
                    last_fireball_time = current_time





    for sprite in all_sprites:
        sprite.update(keys, controller)

    # Draw / render
    screen.fill(BLACK)
    for sprite in all_sprites:
        wall_collisions(sprite , walls)
    walls.draw(screen)


    all_sprites.draw(screen)
    # walls.draw(screen)
    # after drawing everything
    pygame.display.flip()

pygame.quit()


