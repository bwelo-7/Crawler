import pygame
import math
from Bill import Bill
from Bob import Bob
from Controller import KeyboardController
import Projectiles
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
player = Bob(60,70)
enemys = pygame.sprite.Group()
monster = Bill(300,300, target=player)
jim = Bill(700, 600, target=player)

enemys.add(jim)
enemys.add(monster)

all_sprites = pygame.sprite.Group()

all_sprites.add(player)

all_sprites.add(jim)
all_sprites.add(monster)


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

    for sprite in all_sprites:
        if isinstance(sprite, Bob):
            if R2_axis > -0.5 and current_time - last_fireball_time > Fireball_cooldown:
                # avoid divide by zero
                if magnitude > 0.1:
                    dx = (right_x / magnitude) * fireball_speed
                    dy = (right_y / magnitude) * fireball_speed
                else:
                    dx = 0
                    dy = -fireball_speed  # default straight up

                fireball = Projectiles.Fireball(sprite.rect.centerx, sprite.rect.centery, dx=dx, dy=dy)
                all_sprites.add(fireball)
                fireballs.add(fireball)
                last_fireball_time = current_time

    for sprite in all_sprites:
        if isinstance(sprite, Projectiles.Fireball):
            sprite.update(walls)
        else:
            sprite.update(keys, controller)

    for fireball in fireballs:
        if pygame.sprite.spritecollide(fireball, walls, False):
            fireball.kill()


    for fireball in fireballs:
        hits = pygame.sprite.spritecollide(fireball, enemys, False)
        for enemy in hits:
            enemy.take_damage(1)
            fireball.kill()



    for sprite in all_sprites:
        if not isinstance(sprite, Projectiles.Fireball):
            wall_collisions(sprite, walls)

    current_time = pygame.time.get_ticks()


    for bob in all_sprites:
        if isinstance(bob, Bob):
            hits = pygame.sprite.spritecollide(bob, enemys, False)
            if hits:
                if current_time - bob.last_hit_time > bob.hit_cooldown:
                    bob.take_damage(1)
                    bob.last_hit_time = current_time
    print(player.life_status())

    # Draw / render
    screen.fill(BLACK)
    walls.draw(screen)


    all_sprites.draw(screen)
    # walls.draw(screen)
    # after drawing everything
    pygame.display.flip()

pygame.quit()


